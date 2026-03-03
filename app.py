from flask import Flask, render_template, request, redirect, session, flash, send_file
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from datetime import datetime
import os
import io

from config import Config
from models import db, User, FileRecord, Activity
from crypto import encrypt_file, decrypt_file

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# ================= INITIAL SETUP =================
with app.app_context():
    db.create_all()

    # Create default admin
    if not User.query.filter_by(username="admin").first():
        admin = User(
            fullname="Administrator",
            email="admin@securecomm.com",
            phone="0000000000",
            username="admin",
            password_hash=generate_password_hash("Admin@123"),
            role="admin"
        )
        db.session.add(admin)
        db.session.commit()

os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)


# ================= LOGIN =================
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        login_input = request.form.get("login")  # single input field
        password = request.form.get("password")

        # Search by email OR username OR phone
        user = User.query.filter(
            (User.email == login_input) |
            (User.username == login_input) |
            (User.phone == login_input)
        ).first()

        if user and check_password_hash(user.password_hash, password):
            session["user_id"] = user.id
            session["role"] = user.role
            session["fullname"] = user.fullname
            session.permanent = True
            return redirect("/dashboard")
        else:
            flash("Invalid credentials", "error")

    return render_template("login.html")

# ================= SIGNUP =================
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":

        # Prevent duplicate email
        if User.query.filter_by(email=request.form["email"]).first():
            flash("Email already registered!", "error")
            return redirect("/signup")

        user = User(
            fullname=request.form["fullname"],
            email=request.form["email"],
            phone=request.form["phone"],
            username=request.form["username"],
            password_hash=generate_password_hash(request.form["password"]),
            role="user"
        )

        db.session.add(user)
        db.session.commit()

        flash("Account created successfully!", "success")
        return redirect("/")

    return render_template("signup.html")


# ================= DASHBOARD =================
@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect("/")

    if session["role"] == "admin":
        users = User.query.all()
        activities = Activity.query.order_by(Activity.timestamp.desc()).all()
        return render_template("dashboard.html",
                               admin=True,
                               users=users,
                               activities=activities)

    activities = Activity.query.filter_by(
        user_id=session["user_id"]
    ).order_by(Activity.timestamp.desc()).all()

    return render_template("dashboard.html",
                           admin=False,
                           activities=activities)


# ================= ENCRYPT =================
@app.route("/encrypt", methods=["POST"])
def encrypt():
    if "user_id" not in session:
        return redirect("/")

    file = request.files.get("file")
    password = request.form.get("password")

    if not file or not password:
        flash("File and password are required.", "error")
        return redirect("/dashboard")

    try:
        data = file.read()
        encrypted_data = encrypt_file(data, password)

        filename = secure_filename(file.filename) + ".enc"
        filepath = os.path.join(Config.UPLOAD_FOLDER, filename)

        with open(filepath, "wb") as f:
            f.write(encrypted_data)

        # Save record
        record = FileRecord(
            user_id=session["user_id"],
            original_filename=file.filename,
            stored_filename=filename,
            action="encrypt"
        )
        db.session.add(record)

        activity = Activity(
            user_id=session["user_id"],
            action="Encrypted file",
            file_name=file.filename,
            timestamp=datetime.utcnow()
        )
        db.session.add(activity)

        user = User.query.get(session["user_id"])
        user.total_encrypted += 1

        db.session.commit()

        return send_file(
            filepath,
            as_attachment=True,
            download_name=filename
        )

    except Exception:
        flash("Encryption failed. Try again.", "error")
        return redirect("/dashboard")


# ================= DECRYPT =================
@app.route("/decrypt", methods=["POST"])
def decrypt():
    if "user_id" not in session:
        return redirect("/")

    file = request.files.get("file")
    password = request.form.get("password")

    if not file or not password:
        flash("File and password are required.", "error")
        return redirect("/dashboard")

    try:
        data = file.read()
        decrypted_data = decrypt_file(data, password)

        filename = secure_filename(file.filename.replace(".enc", ""))
        output = io.BytesIO(decrypted_data)
        output.seek(0)

        # Save record
        record = FileRecord(
            user_id=session["user_id"],
            original_filename=file.filename,
            stored_filename=filename,
            action="decrypt"
        )
        db.session.add(record)

        activity = Activity(
            user_id=session["user_id"],
            action="Decrypted file",
            file_name=file.filename,
            timestamp=datetime.utcnow()
        )
        db.session.add(activity)

        db.session.commit()

        return send_file(
            output,
            as_attachment=True,
            download_name=filename
        )

    except Exception:
        flash("Incorrect password or corrupted file!", "error")
        return redirect("/dashboard")


# ================= LOGOUT =================
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


# ================= RUN =================
if __name__ == "__main__":

    app.run(debug=True)

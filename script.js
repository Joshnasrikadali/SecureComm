let currentAction = null;

// ===== START ENCRYPT =====
function startEncrypt() {
    currentAction = "encrypt";
    document.getElementById("encryptFile").click();
}

// ===== START DECRYPT =====
function startDecrypt() {
    currentAction = "decrypt";
    document.getElementById("decryptFile").click();
}

// ===== FILE SELECT HANDLER =====
document.getElementById("encryptFile").addEventListener("change", function () {
    if (this.files.length > 0) {
        openModal("Enter Encryption Password");
    }
});

document.getElementById("decryptFile").addEventListener("change", function () {
    if (this.files.length > 0) {
        openModal("Enter Decryption Password");
    }
});

// ===== OPEN MODAL =====
function openModal(title) {
    document.getElementById("modalTitle").innerText = title;
    document.getElementById("modalPassword").value = "";
    document.getElementById("passwordModal").style.display = "flex";
}

// ===== CLOSE MODAL =====
function closeModal() {
    document.getElementById("passwordModal").style.display = "none";
}

// ===== SUBMIT ACTION =====
function submitAction() {
    let password = document.getElementById("modalPassword").value;

    if (!password) {
        alert("Password is required.");
        return;
    }

    if (currentAction === "encrypt") {
        document.getElementById("encryptPassword").value = password;
        document.getElementById("encryptForm").submit();
    }

    if (currentAction === "decrypt") {
        document.getElementById("decryptPassword").value = password;
        document.getElementById("decryptForm").submit();
    }

    closeModal();
}
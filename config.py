import os

class Config:
    SECRET_KEY = "super-secure-production-key"
    SQLALCHEMY_DATABASE_URI = "sqlite:///securecomm.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")
    MAX_CONTENT_LENGTH = 50 * 1024 * 1024  # 50MB
    SESSION_TIMEOUT = 900  # 15 minutes
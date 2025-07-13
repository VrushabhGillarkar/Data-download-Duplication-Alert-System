import os

class Config:
    UPLOAD_FOLDER = './uploads'
    # Only allow the specified extensions, excluding .pptx
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'docx'}
    SECRET_KEY = 'rdx'  # Replace with a real secret key for production
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def is_file_allowed(filename):
        # Check file extension against allowed extensions
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS

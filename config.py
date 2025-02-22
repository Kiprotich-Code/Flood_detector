import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///sensor_data.db')  # Fallback for local dev
    SQLALCHEMY_TRACK_MODIFICATIONS = False
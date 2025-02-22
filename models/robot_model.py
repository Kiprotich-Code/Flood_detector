from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class RobotData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    video_url = db.Column(db.String(255), nullable=False)
    audio_url = db.Column(db.String(255), nullable=False)
    motion = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

    def to_dict(self):
        """Convert SQLAlchemy object to dictionary for JSON serialization."""
        return {
            "id": self.id,
            "video_url": self.video_url,
            "audio_url": self.audio_url,
            "motion": self.motion,
            "timestamp": self.timestamp.strftime("%Y-%m-%d %H:%M:%S")  # Convert datetime to string
        }

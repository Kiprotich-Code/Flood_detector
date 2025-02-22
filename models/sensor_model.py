from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class SensorData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    water_level = db.Column(db.Float, nullable=False)
    air_liquidity = db.Column(db.Float, nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    water_quality = db.Column(db.Float, nullable=False)
    water_conductivity = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<SensorData {self.id}>"

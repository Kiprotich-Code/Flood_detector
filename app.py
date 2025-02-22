from flask import Flask
from config import Config
from models.sensor_model import db
from routes.sensor_routes import sensor_bp
from routes.robot_routes import robot_bp

app = Flask(__name__)
app.config.from_object(Config)

# Initialize database
db.init_app(app)

# Register Blueprints (API endpoints)
app.register_blueprint(sensor_bp)
app.register_blueprint(robot_bp)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Creates tables if they don't exist
    app.run(debug=True)

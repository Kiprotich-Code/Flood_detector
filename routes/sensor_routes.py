from flask import Blueprint, request, jsonify
from repositories.sensor_repository import get_all_sensor_data, get_sensor_data_by_id, create_sensor_data

sensor_bp = Blueprint('sensor', __name__)

@sensor_bp.route('/sensors', methods=['GET'])
def get_sensors():
    """API endpoint to get all sensor data."""
    sensors = get_all_sensor_data()
    return jsonify([sensor.__dict__ for sensor in sensors])

@sensor_bp.route('/sensor/<int:data_id>', methods=['GET'])
def get_sensor(data_id):
    """API endpoint to get a sensor data entry by ID."""
    sensor = get_sensor_data_by_id(data_id)
    if not sensor:
        return jsonify({"error": "Sensor data not found"}), 404
    return jsonify(sensor.__dict__)

@sensor_bp.route('/sensor', methods=['POST'])
def create_sensor():
    """API endpoint to create a new sensor data entry."""
    data = request.json
    required_fields = ["water_level", "air_liquidity", "temperature", "water_quality", "water_conductivity", "latitude", "longitude"]
    
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400
    
    new_id = create_sensor_data(**data)
    return jsonify({"message": "Sensor data created", "id": new_id}), 201

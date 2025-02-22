from flask import Blueprint, jsonify, request
from repositories.robot_repository import get_all_robot_data, get_robot_data_by_id, create_robot_data

robot_bp = Blueprint('robot', __name__, url_prefix='/robot')

@robot_bp.route('/robot', methods=['GET'])
def get_robots():
    """API endpoint to get all robot data."""
    robots = get_all_robot_data()
    return jsonify([robot.to_dict() for robot in robots])

@robot_bp.route('/robot/<int:data_id>', methods=['GET'])
def get_robot(data_id):
    """API endpoint to get a robot data entry by ID."""
    robot = get_robot_data_by_id(data_id)
    if not robot:
        return jsonify({"error": "Robot data not found"}), 404
    return jsonify(robot.to_dict())

@robot_bp.route('/robot/', methods=['POST'])
def add_robot():
    """API endpoint to add new robot data."""
    data = request.get_json()
    if not data or "video_url" not in data or "audio_url" not in data or "motion" not in data:
        return jsonify({"error": "Missing required fields"}), 400
    
    new_id = create_robot_data(
        video_url=data["video_url"],
        audio_url=data["audio_url"],
        motion=data["motion"]
    )
    
    return jsonify({"message": "Robot data created", "id": new_id}), 201

from models.robot_model import RobotData, db

def get_all_robot_data():
    """Fetch all robot data entries."""
    return RobotData.query.all()

def get_robot_data_by_id(data_id):
    """Fetch a single robot data entry by ID."""
    return RobotData.query.get(data_id)

def create_robot_data(video_url, audio_url, motion):
    """Create a new robot data entry."""
    new_robot = RobotData(video_url=video_url, audio_url=audio_url, motion=motion)
    db.session.add(new_robot)
    db.session.commit()
    return new_robot.id  # Return the newly created ID

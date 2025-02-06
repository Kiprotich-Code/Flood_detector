from app import app, db, SensorData  # Import your Flask app and the model
import random

# Function to generate random data
def generate_mock_data():
    mock_data = []
    for _ in range(10):  # Generate 10 mock data entries
        data = SensorData(
            water_level=random.uniform(0.0, 10.0),
            air_liquidity=random.uniform(0.0, 100.0),
            temperature=random.uniform(20.0, 35.0),
            water_quality=random.uniform(0.0, 100.0),
            water_conductivity=random.uniform(0.0, 100.0),
            latitude=random.uniform(-90.0, 90.0),
            longitude=random.uniform(-180.0, 180.0)
        )
        mock_data.append(data)
    return mock_data

# Insert mock data into the database
def seed_database():
    mock_data = generate_mock_data()
    try:
        # Using the application context for database session
        with app.app_context():  # Ensure this block runs inside the app context
            db.session.add_all(mock_data)
            db.session.commit()
            print("Mock data successfully added to the database.")
    except Exception as e:
        db.session.rollback()
        print(f"Error adding mock data: {e}")

if __name__ == "__main__":
    seed_database()

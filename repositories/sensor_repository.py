from models.sensor_model import db, SensorData

def get_all_sensor_data():
    """Fetch all sensor data records."""
    return SensorData.query.all()

def get_sensor_data_by_id(data_id):
    """Fetch a single sensor data record by ID."""
    return SensorData.query.get(data_id)

def create_sensor_data(water_level, air_liquidity, temperature, water_quality, water_conductivity, latitude, longitude):
    """Insert a new sensor data record."""
    new_data = SensorData(
        water_level=water_level,
        air_liquidity=air_liquidity,
        temperature=temperature,
        water_quality=water_quality,
        water_conductivity=water_conductivity,
        latitude=latitude,
        longitude=longitude
    )
    db.session.add(new_data)
    db.session.commit()
    return new_data.id

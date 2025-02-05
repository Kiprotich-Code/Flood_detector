from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flood_detector.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class SensorData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    water_level = db.Column(db.Float, nullable=False)
    air_liquidity = db.Column(db.Float, nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    water_quality = db.Column(db.Float, nullable=False)
    water_conductivity = db.Column(db.Float, nullable=False)
    
    def __repr__(self):
        return f"<SensorData {self.id}>"
    
with app.app_context():
    db.create_all()
    
# receiving data from the ESP32
@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json
    
    new_data = SensorData(
        water_level = data['water_level'],
        air_liquidity = data['air_liquidity'],
        temperature = data['temperature'],
        water_quality = data['water_quality'],
        water_conductivity = data['water_conductivity']
    )
    
    db.session.add(new_data)
    db.session.commit()
    
    return jsonify({"message": "Data received successfully"}), 201

# displaying data
@app.route('/data', methods=['GET'])
def display_data():
    all_data = SensorData.query.all()
    data_list = []
    
    for data in all_data:
        data_dict = {
            "id":data.id,
            "water_level":data.water_level,
            "air_liquidity":data.air_liquidity,
            "temperature":data.temperature,
            "water_quality":data.water_quality,
            "water_conductivity":data.water_conductivity
        }
        
        data_list.append(data_dict)
        
    return jsonify(data_list), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
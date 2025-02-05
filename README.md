# Flood Detector API

This is a simple Flask API that receives and stores sensor data related to water levels, air liquidity, temperature, water quality, and water conductivity. The API supports both data submission (via POST requests) and retrieval (via GET requests).

---

## **📌 Setup Instructions**

### **1. Clone the Repository**
```sh
git clone https://github.com/Navashub/Flood_detector
cd Flood-detector
```

### **2. Create a Virtual Environment (Recommended)**
```sh
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### **3. Install Dependencies**
```sh
pip install -r requirements.txt
```

---

## **🚀 Running the Flask App**

### **4. Set Up Environment Variables (Optional)**
If needed, create a `.env` file and configure environment variables.

### **5. Start the Flask Server**
```sh
python app.py
```
The API should now be running on:
```
http://127.0.0.1:5000
```

---

## **🛠 API Endpoints**

### **1️⃣ Send Data (POST)**
- **URL:** `/data`
- **Method:** `POST`
- **Content-Type:** `application/json`
- **Sample Request Body:**
```json
{
    "water_level": 5.2,
    "air_liquidity": 80.1,
    "temperature": 27.5,
    "water_quality": 95.5,
    "water_conductivity": 0.8
}
```
- **Response:**
```json
{
    "message": "Data received successfully"
}
```

### **2️⃣ Retrieve Data (GET)**
- **URL:** `/data`
- **Method:** `GET`
- **Response Sample:**
```json
[
    {
        "id": 1,
        "water_level": 5.2,
        "air_liquidity": 80.1,
        "temperature": 27.5,
        "water_quality": 95.5,
        "water_conductivity": 0.8
    }
]
```

---

## **🧪 Testing with Postman**
1. Open **Postman**.
2. **POST Request:**
   - Method: `POST`
   - URL: `http://127.0.0.1:5000/data`
   - Body: JSON (see above).
3. **GET Request:**
   - Method: `GET`
   - URL: `http://127.0.0.1:5000/data`
4. Click **Send** and verify responses.

---


## **👤 Author**
- **Navas Herbert**
- GitHub: [Navashub](https://github.com/Navashub)


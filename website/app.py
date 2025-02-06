import streamlit as st 
import requests 

st.title("Flood Detector App Dashboard")

FLASK_SERVER_URL = "http://127.0.0.1:5000/data"

# fetching data from the Flask app
def fetch_data():
    try:
        response = requests.get(FLASK_SERVER_URL)
        if response.status_code == 200:
            return response.json()
        else:
            st.error("Failed to fetch the data from the server.")
            return []
        
    except Exception as e:
        st.error(f"An error occured: {e}")
        return []
    
data = fetch_data()

# displaying data 
if data:
    st.subheader("The Sensor Data")
    st.table(data)
    
# some visualization
if data:
    st.subheader("Visualization")
    
    water_levels = [entry["water_level"] for entry in data]
    temperatures = [entry["temperature"] for entry in data]
    timestamps = [entry["id"] for entry in data]
    
    st.write("Water level over time")
    st.line_chart(water_levels)
    
    # plotting temperatures
    st.write("Tmeperature over Time")
    st.line_chart(temperatures)

else:
    
    st.write("No data available.")



# import streamlit as st
# import requests
# import pandas as pd
# import folium
# from streamlit_folium import folium_static


# # Flask API URL
# API_URL = "http://127.0.0.1:5000/data"

# st.title("🌊 Flood Detector - Sensor Data Collection")

# # Form to collect sensor data
# st.subheader("📌 Enter Sensor Data")
# with st.form("sensor_form"):
#     water_level = st.number_input("Water Level (m)", min_value=0.0, step=0.1)
#     air_liquidity = st.number_input("Air Liquidity (%)", min_value=0.0, step=0.1)
#     temperature = st.number_input("Temperature (°C)", min_value=-50.0, step=0.1)
#     water_quality = st.number_input("Water Quality (%)", min_value=0.0, step=0.1)
#     water_conductivity = st.number_input("Water Conductivity (S/m)", min_value=0.0, step=0.1)
#     latitude = st.number_input("Latitude", format="%.6f")
#     longitude = st.number_input("Longitude", format="%.6f")
    
#     submit_button = st.form_submit_button("Submit Data")

# if submit_button:
#     data = {
#         "water_level": water_level,
#         "air_liquidity": air_liquidity,
#         "temperature": temperature,
#         "water_quality": water_quality,
#         "water_conductivity": water_conductivity,
#         "latitude": latitude,
#         "longitude": longitude
#     }
    
#     response = requests.post(API_URL, json=data)
#     if response.status_code == 201:
#         st.success("✅ Data submitted successfully!")
#     else:
#         st.error("❌ Failed to submit data")

# # Fetching stored data
# st.subheader("📊 View Sensor Data")
# if st.button("Refresh Data"):
#     response = requests.get(API_URL)
#     if response.status_code == 200:
#         data = response.json()
#         df = pd.DataFrame(data)
#         st.dataframe(df)
        
        

#         # Map visualization
#         st.subheader("🗺️ Sensor Data Map")
#         m = folium.Map(location=[df["latitude"].mean(), df["longitude"].mean()], zoom_start=6)
#         for _, row in df.iterrows():
#             folium.Marker(
#                 location=[row["latitude"], row["longitude"]],
#                 popup=f"Water Level: {row['water_level']}m\nTemperature: {row['temperature']}°C"
#             ).add_to(m)
#         folium_static(m)
#     else:
#         st.error("❌ Failed to fetch data")


# import streamlit as st
# import pandas as pd
# import folium
# from streamlit_folium import folium_static
# import plotly.express as px
# import random
# import datetime

# # Function to fetch live data (Mock Example)
# def fetch_live_data():
#     timestamps = [datetime.datetime.now() - datetime.timedelta(minutes=i) for i in range(10)]
#     water_levels = [random.uniform(0.5, 7.5) for _ in range(10)]
#     return pd.DataFrame({"timestamp": timestamps, "water_level": water_levels})

# # Title
# st.title("Flood Detection Cloud Management Platform")

# # Sidebar
# st.sidebar.header("Settings")
# threshold = st.sidebar.slider("Set Flood Threshold (in meters)", 0.0, 10.0, 5.0)

# # Data Monitoring
# st.header("Real-Time Data Monitoring")
# data = fetch_live_data()
# st.line_chart(data.set_index("timestamp"))

# # Google Map Fusion (Ensure latitude/longitude variables exist)
# st.header("Google Map Fusion Display")
# latitude, longitude = 0.0, 0.0  # Default values (Change these)
# sensors = [{"id": 1, "lat": 0.1, "lon": 0.1}, {"id": 2, "lat": 0.2, "lon": 0.2}]  # Example data

# map = folium.Map(location=[latitude, longitude], zoom_start=10)
# for sensor in sensors:
#     folium.Marker(
#         location=[sensor["lat"], sensor["lon"]],
#         popup=f"Sensor {sensor['id']}",
#     ).add_to(map)
# folium_static(map)

# # Alarm Summary
# st.header("Alarm Summary")
# alerts = [{"timestamp": datetime.datetime.now(), "water_level": random.uniform(3.0, 8.0)} for _ in range(5)]
# for alert in alerts:
#     if alert["water_level"] > threshold:
#         st.error(f"🚨 Flood Alert at {alert['timestamp']}: Water level {alert['water_level']}m")

# # Trend Analysis
# st.header("Trend Analysis")
# fig = px.line(data, x="timestamp", y="water_level", title="Water Level Over Time")
# st.plotly_chart(fig)

# # Excel Report
# st.header("Generate Report")
# if st.button("Download Excel Report"):
#     df = pd.DataFrame(data)
#     df.to_excel("flood_report.xlsx", index=False)
#     st.success("Report generated successfully!")
#     with open("flood_report.xlsx", "rb") as file:
#         st.download_button("Download", file, "flood_report.xlsx")



import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
import plotly.express as px
import random
import datetime

# Function to fetch mock live data
def fetch_live_data():
    timestamps = [datetime.datetime.now() - datetime.timedelta(minutes=i) for i in range(10)]
    water_levels = [random.uniform(0.5, 7.5) for _ in range(10)]
    temperature = [random.uniform(15, 35) for _ in range(10)]
    rainfall = [random.uniform(0, 50) for _ in range(10)]
    sensor_ids = [random.choice(["S1", "S2", "S3"]) for _ in range(10)]
    
    # Compute rate of change
    rate_of_change = [0] + [water_levels[i] - water_levels[i - 1] for i in range(1, 10)]

    # Risk level classification
    risk_levels = ["Low" if wl < 3 else "Moderate" if wl < 5 else "High" for wl in water_levels]

    return pd.DataFrame({
        "timestamp": timestamps,
        "sensor_id": sensor_ids,
        "water_level": water_levels,
        "rate_of_change": rate_of_change,
        "temperature": temperature,
        "rainfall": rainfall,
        "risk_level": risk_levels
    })

# Title
st.title("Flood Detection Cloud Management Platform")

# Sidebar
st.sidebar.header("Settings")
threshold = st.sidebar.slider("Set Flood Threshold (in meters)", 0.0, 10.0, 5.0)

# Data Monitoring
st.header("Real-Time Data Monitoring")
data = fetch_live_data()
st.write(data)  # Display DataFrame

# Water Level Line Chart
st.subheader("Water Level Over Time")
fig1 = px.line(data, x="timestamp", y="water_level", color="sensor_id", title="Water Levels per Sensor")
st.plotly_chart(fig1)

# Rate of Change Visualization
st.subheader("Rate of Change in Water Level")
fig2 = px.bar(data, x="timestamp", y="rate_of_change", color="sensor_id", title="Water Level Rate of Change")
st.plotly_chart(fig2)

# Rainfall vs. Water Level
st.subheader("Rainfall vs Water Level")
fig3 = px.scatter(data, x="rainfall", y="water_level", color="risk_level", size="rainfall", title="Impact of Rainfall on Water Levels")
st.plotly_chart(fig3)

# Google Map Fusion (Ensure latitude/longitude exist)
st.header("Google Map Fusion Display")
latitude, longitude = -1.286389, 36.817223  # Example location (Nairobi)
sensors = [{"id": "S1", "lat": -1.285, "lon": 36.818}, {"id": "S2", "lat": -1.287, "lon": 36.819}]

map = folium.Map(location=[latitude, longitude], zoom_start=10)
for sensor in sensors:
    folium.Marker(
        location=[sensor["lat"], sensor["lon"]],
        popup=f"Sensor {sensor['id']}",
    ).add_to(map)
folium_static(map)

# Alarm Summary
st.header("Alarm Summary")
for _, alert in data.iterrows():
    if alert["water_level"] > threshold:
        st.error(f"🚨 Flood Alert at {alert['timestamp']} from Sensor {alert['sensor_id']}! Water Level: {alert['water_level']}m")

# Excel Report
st.header("Generate Report")
if st.button("Download Excel Report"):
    df = pd.DataFrame(data)
    df.to_excel("flood_report.xlsx", index=False)
    st.success("Report generated successfully!")
    with open("flood_report.xlsx", "rb") as file:
        st.download_button("Download", file, "flood_report.xlsx")

from supabase import create_client, Client
import app

SUPABASE_URL = app.SUPABASE_URL
SUPABASE_KEY = app.SUPABASE_KEY

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Define data as a list of dictionaries
data = [
    {"water_level": 12.5, "air_liquidity": 85.2, "temperature": 28.5, "water_quality": 90.1, "water_conductivity": 45.6, "latitude": -1.286389, "longitude": 36.817223},
]

# Insert data into Supabase
response = supabase.table("sensor_data").insert(data).execute()

# Print response
print(response)

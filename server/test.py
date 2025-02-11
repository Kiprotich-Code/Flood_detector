import requests
import app

SUPABASE_URL = app.SUPABASE_URL
SUPABASE_KEY = app.SUPABASE_KEY

headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json"
}

# Correct API request
response = requests.get(f"{SUPABASE_URL}/rest/v1/sensor_data", headers=headers)

print(response.status_code, response.text)

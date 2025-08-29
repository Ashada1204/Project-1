import requests
import pandas as pd
from datetime import datetime

# --- CONFIG ---
API_KEY = "5a184740fe35f36ef0741073c17bde99"   # replace with your actual key
CITY = "Pune"
CSV_FILE = "weather_data.csv"
REPORT_FILE = "weather_report.html"

def fetch_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid=5a184740fe35f36ef0741073c17bde99&units=metric"

    response = requests.get(url)
    response.raise_for_status()  # raise error if request fails
    data = response.json()
    records = []

    for item in data["list"]:
        dt = datetime.fromtimestamp(item["dt"])
        temp = item["main"]["temp"]
        records.append({"date": dt.date(), "temp": temp})

    return pd.DataFrame(records)

# --- Main ---
df = fetch_weather(CITY, API_KEY)
df.to_csv(CSV_FILE, index=False)

# Daily stats
summary = df.groupby("date")["temp"].agg(["mean", "min", "max"])
summary.to_html(REPORT_FILE)

print("✅ Weather report generated:", REPORT_FILE)

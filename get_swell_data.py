import make_api_call as call
import duckdb
import json
import os


# openmeteo api
# https://open-meteo.com/en/docs
# base url
url = "https://marine-api.open-meteo.com/v1/marine"

# duckdb setup
conn = duckdb.connect('locations.duckdb')
locations = conn.execute("SELECT * FROM locations").fetchdf()

loc = locations['location'].to_list()
lat = locations['lat'].to_list()
long = locations['long'].to_list()

# api parameters
params = {
    "latitude": None,
    "longitude": None,
    "hourly": ["wave_height", "wave_direction", "wave_period", "swell_wave_height", "swell_wave_direction", "swell_wave_period"],
    "timezone": "Australia/Sydney",
    "forecast_days": 7
}

# loop through locations and make api call
for lat, long, loc in zip(lat, long, loc):
    updated_params = params.copy()
    updated_params["latitude"] = lat
    updated_params["longitude"] = long

    # calling api function
    data = call.make_api_call(url, updated_params)

    # save to landing zone
    with open(os.path.join('landing_zone',f'{loc}_data.json'), 'w') as json_file:
        json.dump(data, json_file, indent=1)





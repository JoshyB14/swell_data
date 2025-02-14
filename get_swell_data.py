import make_api_call as call
import json
import os


# openmeteo api
# https://open-meteo.com/en/docs

# base url
url = "https://marine-api.open-meteo.com/v1/marine"

# parameters for Freshwater Beach on Sydney's Northern Beaches
params = {
	"latitude": -33.784387,
	"longitude": 151.294499,
	"hourly": ["wave_height", "wave_direction", "wave_period", "swell_wave_height", "swell_wave_direction", "swell_wave_period"],
	"timezone": "Australia/Sydney",
	"forecast_days": 7
}

# calling api function
freshwater_data = call.make_api_call(url, params)

# save to landing zone
with open(os.path.join('landing_zone','freshwater_data.json'), 'w') as json_file:
    json.dump(freshwater_data, json_file, indent=1)





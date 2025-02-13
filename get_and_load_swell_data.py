import make_api_call as call

# Openmeteo api
# https://open-meteo.com/en/docs

# Base url
url = "https://marine-api.open-meteo.com/v1/marine"

# Parameters for Freshwater Beach on Sydney's Northern Beaches
params = {
	"latitude": -33.784387,
	"longitude": 151.294499,
	"hourly": ["wave_height", "wave_direction", "wave_period", "swell_wave_height", "swell_wave_direction", "swell_wave_period"],
	"timezone": "Australia/Sydney",
	"forecast_days": 1
}

# Calling api function
freshwater_data = call.make_api_call(url, params)





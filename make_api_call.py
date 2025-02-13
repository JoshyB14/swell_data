import time
import requests

# Function to make the API call with retry mechanism
def make_api_call(url, params, retries=5, wait_time=5):
    attempt = 0
    while attempt < retries:
        try:
            # Make the GET request
            response = requests.get(url, params=params, verify=False)
            
            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Parse the JSON data if the response is successful
                data = response.json()
                return data
            else:
                # Handle unsuccessful requests (e.g., 4xx, 5xx errors)
                print(f"Request failed with status code: {response.status_code}")
        
        except requests.exceptions.RequestException as e:
            # Catch exceptions like network errors, timeout, etc.
            print(f"Error during API call: {e}")
        
        # Increment attempt and wait before retrying
        attempt += 1
        print(f"Retrying in {wait_time} seconds... (Attempt {attempt}/{retries})")
        time.sleep(wait_time)  # Wait before retrying
        wait_time *= 2  # Exponential backoff (increase wait time with each retry)
    
    # If the retries are exhausted, return None or handle failure
    print(f"Failed to get data after {retries} retries.")
    return None
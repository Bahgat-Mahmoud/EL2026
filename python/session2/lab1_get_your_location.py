"""Write a Python program to get info about your location."""

import time
import requests

def get_info_location():
    """Write your solution here. Don't forget to return the result at the end."""
    url = "https://ipinfo.io/json"
    # response = requests.get(url, timeout=5)
    # return response.json()
    #######################################
    # Implementing retry logic for handling timeouts
    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=5)
            data = response.json()
            return data
        except requests.exceptions.Timeout:
            print(f"Timeout... retry {attempt + 1}/{max_retries}")
            time.sleep(2)
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            break
    return {}
    #######################################


if __name__ == "__main__":
    location_info = get_info_location()
    assert "ip" in location_info, "Test case failed"
    assert "city" in location_info, "Test case failed"
    assert "region" in location_info, "Test case failed"
    assert "country" in location_info, "Test case failed"
    assert "loc" in location_info, "Test case failed"
    assert "org" in location_info, "Test case failed"

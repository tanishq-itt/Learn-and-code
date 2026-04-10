import requests
from config import Config
from exceptions import GeocodingError

class GoogleGeocoder:
    BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"

    def __init__(self, api_key: str = Config.GOOGLE_API_KEY):
        self.api_key = api_key

    def get_coordinates(self, location: str):
        params = {
            "address": location,
            "key": self.api_key
        }

        try:
            response = requests.get(self.BASE_URL, params=params, timeout=5)
            data = response.json()
        except requests.RequestException as e:
            raise GeocodingError(f"API request failed: {e}")

        if data.get("status") != "OK":
            raise GeocodingError(f"API Error: {data.get('status')}")

        return self._extract_results(data)

    def _extract_results(self, data):
        results = []

        for item in data.get("results", []):
            results.append({
                "formatted_address": item.get("formatted_address"),
                "latitude": item["geometry"]["location"]["lat"],
                "longitude": item["geometry"]["location"]["lng"]
            })

        if not results:
            raise GeocodingError("No results found.")

        return results
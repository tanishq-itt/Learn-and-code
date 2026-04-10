from validator import validate_location
from geocoder import GoogleGeocoder
from formatter import format_results
from exceptions import InvalidInputError, GeocodingError


def main():
    try:
        location = input("Enter location: ")

        validated_location = validate_location(location)

        geocoder = GoogleGeocoder()
        results = geocoder.get_coordinates(validated_location)

        output = format_results(results)
        print("\n=== Results ===")
        print(output)

    except InvalidInputError as e:
        print(f"Input Error: {e}")

    except GeocodingError as e:
        print(f"Geocoding Error: {e}")

    except Exception as e:
        print(f"Unexpected Error: {e}")


if __name__ == "__main__":
    main()
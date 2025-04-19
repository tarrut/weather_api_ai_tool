from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import httpx
import os
import sys

load_dotenv()

mcp = FastMCP("WEATHER")

load_dotenv()
api_key = os.getenv("WEATHER_API_KEY")

@mcp.tool()  
def get_weather(location: str) -> dict:
    """
    Retrieve current weather data for a specified location.

    Makes an HTTP request to the WeatherAPI and returns current weather
    conditions including temperature, humidity, wind speed, and more.

    Args:
        location (str): The location to get weather data for. Can be a city
            name, latitude/longitude coordinates, US zip code, UK postcode,
            Canada postal code, or IP address.

    Returns:
        dict: A dictionary containing current weather information with keys
            such as 'temp_c', 'temp_f', 'condition', 'wind_mph', 'wind_kph',
            'humidity', etc.

    Raises:
        SystemExit: If there's a network error or invalid API response.
    """

    url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": api_key,
        "q": location,
    }

    try:
        response = httpx.get(url, params=params, timeout=10.0)
        response.raise_for_status()
    except httpx.RequestError as e:
        print(f"Network error while requesting weather: {e}", file=sys.stderr)
        sys.exit(1)
    except httpx.HTTPStatusError as e:
        print(f"Error response {e.response.status_code} from weather API: {e}", file=sys.stderr)
        sys.exit(1)

    data = response.json()
    current = data.get("current", {})
    return current


if __name__ == "__main__":
    mcp.run(transport="stdio")
# WEATHER MCP Server

This project implements a simple MCP server for retrieving **current weather data** using the [WeatherAPI](https://www.weatherapi.com/).  


## Tool: `get_weather`

**Signature**:
```python
get_weather(location: str) -> dict
```

**Description**:  
Retrieves current weather conditions for the specified location.

- **Input**:  
  - `location` (str): City name, latitude/longitude, ZIP/postal code, or IP address.
- **Output**:  
  A dictionary containing weather data such as:
  - `temp_c` (temperature in Celsius)
  - `temp_f` (temperature in Fahrenheit)
  - `condition` (weather condition text and icon)
  - `wind_mph`, `wind_kph` (wind speed)
  - `humidity` (percentage)
  - And more!

**Example Response**:
```json
{
  "temp_c": 22.0,
  "temp_f": 71.6,
  "condition": {
    "text": "Partly cloudy",
    "icon": "//cdn.weatherapi.com/weather/64x64/day/116.png"
  },
  "wind_mph": 5.6,
  "wind_kph": 9.0,
  "humidity": 65
}
```

## License

This project is licensed under the MIT License.

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


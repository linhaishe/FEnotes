"""Shared Open-Meteo weather tool."""

import json
from urllib.parse import urlencode
from urllib.request import urlopen


# urlencode 自动进行 URL 编码，避免中文、空格和特殊字符破坏 URL
def _get_json(url: str, params: dict) -> dict:
    with urlopen(f"{url}?{urlencode(params)}", timeout=10) as response:
        return json.load(response)


def get_weather(city: str) -> dict:
    city = city.strip()  # 作用是去掉城市名称前后的空白字符
    if not city:
        raise ValueError("city must not be empty")

    locations = _get_json(
        "https://geocoding-api.open-meteo.com/v1/search",
        {"name": city, "count": 1, "language": "zh", "format": "json"},
    ).get("results", [])
    if not locations:
        raise ValueError(f"city not found: {city}")

    location = locations[0]
    forecast = _get_json(
        "https://api.open-meteo.com/v1/forecast",
        {
            "latitude": location["latitude"],
            "longitude": location["longitude"],
            "current": "temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m",
            "timezone": "auto",
        },
    )
    return {
        "city": location["name"],
        "country": location.get("country", ""),
        "timezone": forecast.get("timezone", ""),
        "current": forecast["current"],
        "units": forecast["current_units"],
    }

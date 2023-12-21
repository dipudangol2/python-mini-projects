import json
import datetime
from data_scraper import get_weather_data

CURRENT_YEAR = datetime.datetime.now().year
weather_data = {}
MONTHS = {
    "1": "Jan",
    "2": "Feb",
    "3": "Mar",
    "4": "Apr",
    "5": "May",
    "6": "Jun",
    "7": "Jul",
    "8": "Aug",
    "9": "Sep",
    "10": "Oct",
    "11": "Nov",
    "12": "Dec",
}

url = "https://www.accuweather.com/en/np/thankot/241832/daily-weather-forecast/241832"


weather_data = get_weather_data(url, MONTHS, CURRENT_YEAR)


with open("data.json", "w") as jsonfile:
    jsonfile.write(json.dumps(weather_data, indent=4))
    jsonfile.close()

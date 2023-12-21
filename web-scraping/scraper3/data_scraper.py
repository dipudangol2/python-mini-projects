import requests
from bs4 import BeautifulSoup



def get_weather_data(url, months, year):
    all_data = {}
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
        "Accept-Encoding": "*",
        "Connection": "keep-alive",
    }

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "lxml")

    info_div = soup.find("div", class_="page-content content-module")

    weather_div = info_div.find_all("div", class_="daily-wrapper")

    for i in range(0, len(weather_div)):
        info_dict = {}

        date_obj = (
            weather_div[i]
            .find("h2", class_="date")
            .text.strip()
            .replace("\n", " ")
            .split(" ")
        )
        temp = weather_div[i].find("div", class_="temp").get_text(strip=True).split("/")
        month_day = date_obj[1].split("/")
        info_dict["date"] = {
            "day_name": date_obj[0],
            "day": month_day[1],
            "month": months[month_day[0]],
            "year": year,
        }
        info_dict["temp"] = {
            "min": temp[-1] + "C",
            "max": temp[0] + "C",
        }
        info_dict["precipitation"] = (
            weather_div[i].find("div", class_="precip").get_text(strip=True)
        )

        info_dict["phrase"] = (
            weather_div[i].find("div", class_="phrase").get_text(strip=True)
        )

        panel_items = weather_div[i].find("div", class_="panels").find_all("div")

        info_dict["panel-items"] = {
            "1": panel_items[0]
            .find_all("p", class_="panel-item")[0]
            .get_text(separator=" : ", strip=True),
            "2": panel_items[0]
            .find_all("p", class_="panel-item")[1]
            .get_text(separator=" : ", strip=True),
            "3": panel_items[1]
            .find_all("p", class_="panel-item")[0]
            .get_text(separator=" : ", strip=True),
            "4": panel_items[1]
            .find_all("p", class_="panel-item")[1]
            .get_text(separator=" : ", strip=True),
        }
        all_data[i] = info_dict
    return all_data

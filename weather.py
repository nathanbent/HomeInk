
# Grab info from OWM to display
# Info pulled: - 48 hour forecast, - today high + low, - Description now + forecast

import matplotlib.pyplot as plt
import numpy as np
import requests
import json
from datetime import datetime
import screen_tools

screen_width = 600
screen_height = 448

api_key = "455989e3f6195a09259e06f612fa7731"
lat = "38.658173"
lon = "-77.249702"
url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=imperial" % (lat, lon, api_key)

def owm_request_string():
    response = requests.get(url)
    data = json.loads(response.text)
    return data

def owm_request_parser(data, metric_to_parse):

    if metric_to_parse == "forecast":
        fc_times = []
        fc_temps = []
        hourly = data["hourly"]
        for entry in hourly:  # Set up tables for forecast
            dt = datetime.utcfromtimestamp(entry["dt"])
            fc_times.append(dt)
            temp = entry["temp"]
            fc_temps.append(temp)
        return fc_times, fc_temps
    elif metric_to_parse == "current":
        # get current dict block
        current = data['current']
        # get current
        temp_current = current['temp']
        # get feels like
        feels_like = current['feels_like']
        # get humidity
        humidity = current['humidity']
        # get pressure
        wind = current['wind_speed']
        # get description
        weather = current['weather']
        report = weather[0]['description']
        # get icon url
        icon_code = weather[0]['icon']
        # icon_URL = 'http://openweathermap.org/img/wn/'+ icon_code +'@4x.png'
        return temp_current, feels_like, humidity, wind, report, icon_code

    elif metric_to_parse == "daily":
        # get daily dict block
        daily = data['daily']
        # get daily precip
        daily_precip_float = daily[0]['pop']
        # format daily precip
        daily_precip_percent = daily_precip_float * 100
        # get min and max temp
        daily_temp = daily[0]['temp']
        temp_max = daily_temp['max']
        temp_min = daily_temp['min']
        return daily_precip_percent, temp_min, temp_max

def owm_graph_create(graph_dataset_one, graph_dataset_two, graph_dataset_metric):  # Dataset one should be TIME
    plt.plot(graph_dataset_one, graph_dataset_two)
    plt.show()

def main():
    while True:
        time_pulled = datetime.now()
        data = owm_request_string()
        fc_times, fc_temps = owm_request_parser(data, "forecast")
        temp_current, feels_like, humidity, wind, report, icon_code = owm_request_parser(data, "current")
        daily_precip_percent, temp_min, temp_max = owm_request_parser(data, "daily")
        print(time_pulled)

        blank_screen = screen_tools.create_blank_background(screen_width, screen_height)
        black_lines = ImageDraw.Draw(blank_screen)  # White box
        black_lines.line((0, 15, screen_width, 15), fill=(0, 0, 0, 255))  # Line below times
        now = datetime.now()  # Load the current time to show on display
        date_text = now.strftime("%A, %B, %d")  # The date text
        black_lines.text((0, 0), "Screen updated on " + date_text + " at " + str(now.strftime("%I:%M %p")),
                         font= font18, fill=(0, 0, 0, 255))  # Screen updated section





main()
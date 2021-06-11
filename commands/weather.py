import datetime
import json

import weathercom
from command import Command

week = [
    "sunday",
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
]


class Weather(Command):
    def __init__(self, comm):
        super().__init__(comm)
        self.aliases = ["weather {date| }", "weather"]

    def _execute(self):
        say = ""
        data = json.loads(
            weathercom.getCityWeatherDetails(
                city="bangalore", queryType="ten-days-data"
            )
        )["vt1dailyForecast"]["day"]["narrative"]

        v = self.values.get("date")
        if v:
            date, days = v
            now = int(datetime.datetime.now().strftime("%w"))
            for d in range(0, days):
                x = (now + date + d) % 7

                say += f"On {week[x]}: {data[date + d]} "
        else:
            say = data[0]

        return (
            False,
            say,
            None,
        )

import json

import weathercom
from arguments.date import now, week
from command import Command
from settings import Settings


class Weather(Command):
    def __init__(self):
        super().__init__()
        self.aliases = ["weather {date| }", "weather"]

    def _execute(self):
        say = ""
        data = json.loads(
            weathercom.getCityWeatherDetails(
                city=Settings.getInstance().get("weatherCity"),
                queryType="ten-days-data",
            )
        )["vt1dailyForecast"]["day"]["narrative"]

        v = self.values.get("date")
        if v:
            date, days = v
            for d in range(0, days):
                x = (now() + date + d) % 7

                say += f"On {week[x]}: {data[date + d]} "
        else:
            say = data[0]

        return (
            False,
            say,
            None,
        )

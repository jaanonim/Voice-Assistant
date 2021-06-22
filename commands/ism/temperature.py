import requests
from classes.command import Command
from utilities.settings import Settings


class Temperature(Command):
    def __init__(self):
        super().__init__()
        self.aliases = ["What's the temperature {thermometer|Where?}"]

    def _execute(self):

        if self.values["thermometer"] == 0:
            url = str(Settings.getInstance().get("ismaAdres")) + "/api"
            try:
                data = self.makeRequest(url)
                if not data:
                    raise
                temp = f'in aquarium: {data["Temp"]} degrees'
            except:
                return False, "Something went wrong.", None

        elif self.values["thermometer"] == 1:
            url = str(Settings.getInstance().get("ismpAdres")) + "/api"
            try:
                data = self.makeRequest(url)
                if not data:
                    raise
                temp = f'inside: {data["Temp_in"]} degrees'
            except:
                return False, "Something went wrong.", None

        else:
            url = str(Settings.getInstance().get("ismpAdres")) + "/api"
            try:
                data = self.makeRequest(url)
                if not data:
                    raise
                temp = f'outside: {data["Temp_out"]} degrees'
            except:
                return False, "Something went wrong.", None

        return False, f"The temperature {temp}", None

    def makeRequest(self, url):
        try:
            return requests.get(url).json()
        except:
            return None

import json
import sys


class Settings:
    __instance = None

    @staticmethod
    def getInstance():
        if Settings.__instance == None:
            Settings()
        return Settings.__instance

    def __init__(self):

        if Settings.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            self.file_name = None
            Settings.__instance = self

        if not self.file_name:
            try:
                self.file_name = str(sys.argv[1])
            except:
                self.file_name = "settings.json"

        self.data = {}
        try:
            f = open(self.file_name)
            self.data = json.load(f)
            f.close()
            if self.data == {}:
                raise Exception
        except Exception as e:
            print("[ENGINE] Cannot found " + self.file_name)

    def get(self, name):
        return self.data.get(name)

    def set(self, name, value):
        self.data[name] = value
        with open(self.file_name, "w") as json_file:
            json.dump(self.data, json_file)

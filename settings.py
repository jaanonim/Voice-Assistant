import json

file_name = "settings.json"


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
            Settings.__instance = self

        self.data = {}
        try:
            f = open(file_name)
            self.data = json.load(f)
            f.close()
            if self.data == {}:
                raise Exception
        except Exception as e:
            print("Cannot found " + file_name)
            with open(file_name, "w") as json_file:
                json.dump({}, json_file)

    def get(self, name):
        return self.data.get(name)

    def set(self, name, value):
        self.data[name] = value
        with open(file_name, "w") as json_file:
            json.dump(self.data, json_file)

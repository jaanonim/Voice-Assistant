class Cache:
    __instance = None

    @staticmethod
    def getInstance():
        if Cache.__instance == None:
            Cache()
        return Cache.__instance

    def __init__(self):

        if Cache.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Cache.__instance = self
        self.data = {}

    def get(self, name):
        return self.data.get(name)

    def set(self, name, value):
        self.data[name] = value

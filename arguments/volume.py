from classes.argument import Argument


class Volume(Argument):
    @staticmethod
    def get_value(value):
        words = value.strip().split(" ")
        values = []
        for i in range(0, len(words)):
            try:
                n = int(words[i])
            except:
                n = None
            if n:
                if n >= 0 and n <= 100:
                    return n
        return None

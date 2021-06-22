from classes.argument import Argument


class Thermometer(Argument):
    @staticmethod
    def get_value(value):
        if "aquarium" in value:
            return 0

        if "inside" in value:
            return 1

        if "outsite" in value or "outside" in value:
            return 2

        return None

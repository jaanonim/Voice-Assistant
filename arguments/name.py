from classes.argument import Argument


class Name(Argument):
    @staticmethod
    def get_value(value):
        return value.strip()

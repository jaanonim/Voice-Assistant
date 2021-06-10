from argument import Argument


class OnOff(Argument):
    @staticmethod
    def get_value(value):
        if "on" in value:
            return True

        if "off" in value:
            return False

        return None

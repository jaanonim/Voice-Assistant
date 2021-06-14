import datetime

from classes.argument import Argument

week = [
    "sunday",
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
]


def now():
    return int(datetime.datetime.now().strftime("%w"))


class Date(Argument):
    @staticmethod
    def get_value(value):

        if "today" in value:
            return 0, 1

        if "tomorrow" in value:
            return 1, 1

        n = now()
        days = 1
        date = 0

        if "next" in value:
            date += 7

        if "weekend" in value:
            days = 3
            if n == 1:
                date += 4
            elif n == 2:
                date += 3
            elif n == 3:
                date += 2
            elif n == 4:
                date += 1

        elif "week" in value:
            days = 7

        else:
            for i in range(0, 7):
                if week[i] in value:
                    x = i - n
                    if x <= 0:
                        x += 7
                    date += x

        return date, days

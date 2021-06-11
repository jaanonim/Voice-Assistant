import datetime

from argument import Argument

week = [
    "sunday",
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
]


class Date(Argument):
    @staticmethod
    def get_value(value):

        if "today" in value:
            return 0, 1

        if "tomorrow" in value:
            return 1, 1

        now = int(datetime.datetime.now().strftime("%w"))
        days = 1
        date = 0

        if "next" in value:
            date += 7

        if "weekend" in value:
            days = 3
            if now == 1:
                date += 4
            elif now == 2:
                date += 3
            elif now == 3:
                date += 2
            elif now == 4:
                date += 1

        elif "week" in value:
            days = 7

        else:
            for i in range(0, 7):
                if week[i] in value:
                    x = i - now
                    if x <= 0:
                        x += 7
                    date += x

        return date, days

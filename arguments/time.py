from classes.argument import Argument

UNITS = [("day", 86400), ("hour", 3600), ("minute", 60), ("second", 1)]


def get_multiplayer(v):
    for u in UNITS:
        name, multi = u
        if name in v:
            return u


class Time(Argument):
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
                values.append((get_multiplayer(words[i + 1]), n))

        length = 0
        toSpeach = []
        if len(values) > 0:
            for v in values:
                x, num = v
                name, multi = x
                length += num * multi
                if num > 1:
                    name += "s"
                toSpeach.append((num * multi, str(num) + " " + name))

        toSpeach.sort(reverse=True, key=lambda v: v[0])
        output = ""
        if len(toSpeach) > 1:
            for i in range(0, len(toSpeach)):
                output += toSpeach[i][1] + " "
                if i == len(toSpeach) - 2:
                    output += "and "
            output = output.strip()
        else:
            output = toSpeach[0][1]

        if length != 0:
            return (length, output)

        return None

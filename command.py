import re

from loader import get_class


class Command:
    def __init__(self, comm):
        self.comm = f" {comm} "
        self.aliases = []
        self.cuurent_alias = None

    def to_regex(self, alias):
        return re.split("{.*}", alias), re.findall("{.*}", alias)

    def check(self):
        for a in self.aliases:
            reg, args = self.to_regex(f" {a} ")
            if re.search(".*".join(reg), self.comm):
                self.args = []
                for i in range(0, len(args)):
                    v = re.findall(f"{reg[i]}.*{reg[i+1]}", self.comm)[0]
                    v = v.replace(reg[i], "")
                    v = v.replace(reg[i + 1], "")
                    self.args.append((args[i].replace("{", "").replace("}", ""), v))
                self.cuurent_alias = a
                return True
        return False

    def validate_args(self):
        self.values = []

        for arg in self.args:
            name, value = arg
            obj = get_class("arguments", name)
            if obj:
                v = obj.get_value(value)
                if v is None:
                    return arg
                else:
                    self.values.append(v)
            else:
                raise NameError(
                    f"Cannont find file named {name}.py with correct class name in argumments!"
                )
        return None

    def execute(self):
        invalid = self.validate_args()
        if invalid:
            return True, None, invalid
        return self._execute()

    def _execute(self):
        pass

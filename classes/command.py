import re

from network.server import Server
from utilities.loader import get_class


class Command:
    def __init__(self):
        self.aliases = []
        self.target = "server"

    def to_regex(self, alias):
        return re.split("{.*}", alias), re.findall("{.*}", alias)

    def check(self, comm):
        comm = f" {comm.lower()} "
        for a in self.aliases:
            reg, args = self.to_regex(f" {a.lower()} ")
            if re.search(".*".join(reg), comm):
                self.args = []
                for i in range(0, len(args)):
                    v = re.findall(f"{reg[i]}.*{reg[i+1]}", comm)[0]
                    v = v.replace(reg[i].strip(), "")
                    v = v.replace(reg[i + 1].strip(), "")
                    name, resp = args[i].replace("{", "").replace("}", "").split("|")
                    self.args.append((name, v, resp))
                return True
        return False

    def validate_args(self):
        self.values = {}
        for arg in self.args:
            name, value, resp = arg
            obj = get_class("arguments", name)
            if obj:
                v = obj.get_value(value)
                if v is None:
                    return resp, obj
                else:
                    self.values[name] = v
            else:
                raise NameError(
                    f"Cannont find file named {name}.py with correct class name in argumments!"
                )
        return None

    def execute(self):
        invalid = self.validate_args()
        if invalid:
            resp, obj = invalid
            return True, resp, obj
        return self.exec_target()

    def exec_target(self):
        if self.target == "server":
            return self._execute()

        else:
            return Server.getInstance().sendCommand(
                self.target, self.__class__.__module__, self.values
            )

    def _execute(self):
        pass

class Argument:
    def __init__(self, comm):
        self.comm = comm
        self.aliases = []
        self.require = False

    def in_comm(self):
        if len(self.aliases) == 0:
            return True
        for a in self.aliases:
            if a in self.comm:
                return True
        return False

    def value(self):
        pass

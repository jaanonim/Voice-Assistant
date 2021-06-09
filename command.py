class Command:
    def __init__(self, comm):
        self.comm = comm
        self.aliases = []
        self.args = []

    def check(self):
        for a in self.aliases:
            if a in self.comm:
                return True
        return False

    def validate_args(self):
        self.values = []
        for arg in self.args:
            if not arg.in_comm(comm):
                if arg.require:
                    return arg
            else:
                self.values.append(arg)
        return None

    def execute(self):
        invalid = self.validate_args()
        if invalid:
            return True, None, invalid
        return self._execute()

    def _execute(self):
        pass

class BaseAgent:
    def __init__(self, name):
        self.name = name

    def can_run(self, state):
        raise NotImplementedError

    def run(self, state):
        raise NotImplementedError


class BaseAgent:
    """
    Base class for all agents in the system.
    Every agent must implement the run() method.
    """

    def run(self, input_data):
        raise NotImplementedError("Agents must implement the run() method")


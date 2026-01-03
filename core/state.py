class SharedState:
    def __init__(self, product_data):
        self.data = {
            "raw_product": product_data,
            "parsed_product": None,
            "questions": None,
            "pages": {},
            "completed_agents": set()
        }

    def mark_completed(self, agent_name):
        self.data["completed_agents"].add(agent_name)

    def is_completed(self, agent_name):
        return agent_name in self.data["completed_agents"]


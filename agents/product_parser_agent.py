from agents.base_agent import BaseAgent
from data.product_input import product_data

class ProductParserAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="ProductParserAgent")

    def can_run(self, state):
        return not hasattr(state, "parsed_product")

    def run(self, state):
        # Convert raw product data to parsed object
        parsed_product = product_data  # Can expand processing if needed
        state.parsed_product = parsed_product
        print("ProductParserAgent: Parsed product added to state.")


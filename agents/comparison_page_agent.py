from agents.base_agent import BaseAgent
from templates.comparison_template import build_comparison_template
from logic_blocks.comparison_block import compare_ingredients_block

class ComparisonPageAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="ComparisonPageAgent")

    def can_run(self, state):
        return hasattr(state, "parsed_product") and "comparison" not in getattr(state, "data", {}).get("pages", {})

    def run(self, state):
        product_a = state.parsed_product
        # Dummy product for comparison
        product_b = {"Product Name": "Product B", "Ingredients": []}

        comparison = compare_ingredients_block(product_a, product_b)
        comparison_page = build_comparison_template(product_a, product_b, comparison)

        if not hasattr(state, "data"):
            state.data = {"pages": {}}
        state.data["pages"]["comparison"] = comparison_page

        print("ComparisonPageAgent: Comparison page added to state.")


from agents.base_agent import BaseAgent
from templates.comparison_template import build_comparison_template

class ComparisonPageAgent(BaseAgent):
    """
    Agent responsible for assembling the comparison page.
    """

    def run(self, product):
        fictional_product_b = {
            "name": "Radiant C Serum",
            "ingredients": ["Vitamin C", "Niacinamide"],
            "benefits": ["Brightening"],
            "price": "₹799"
        }

        return {
            "page_type": "Comparison",
            "content": build_comparison_template(product, fictional_product_b)
        }


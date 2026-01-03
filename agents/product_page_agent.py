from agents.base_agent import BaseAgent
from templates.product_template import build_product_template
from logic_blocks.usage_block import generate_usage_block
from logic_blocks.benefits_block import generate_benefits_block

class ProductPageAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="ProductPageAgent")

    def can_run(self, state):
        return hasattr(state, "parsed_product") and "product" not in getattr(state, "data", {}).get("pages", {})

    def run(self, state):
        product = state.parsed_product
        product_page = build_product_template(
            product,
            usage=generate_usage_block(product),
            benefits=generate_benefits_block(product)
        )

        if not hasattr(state, "data"):
            state.data = {"pages": {}}
        state.data["pages"]["product"] = product_page

        print("ProductPageAgent: Product page added to state.")


from agents.base_agent import BaseAgent
from templates.product_template import build_product_template

class ProductPageAgent(BaseAgent):
    """
    Agent responsible for assembling the product page.
    """

    def run(self, product):
        return {
            "page_type": "Product",
            "content": build_product_template(product)
        }


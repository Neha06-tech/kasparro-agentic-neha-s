from agents.base_agent import BaseAgent

class ProductParserAgent(BaseAgent):
    """
    Agent responsible for parsing raw product data
    into a clean internal representation.
    """

    def run(self, product_data):
        parsed_product = {
            "name": product_data["Product Name"],
            "concentration": product_data["Concentration"],
            "skin_type": product_data["Skin Type"],
            "ingredients": product_data["Key Ingredients"],
            "benefits": product_data["Benefits"],
            "usage": product_data["How to Use"],
            "side_effects": product_data["Side Effects"],
            "price": product_data["Price"]
        }

        return parsed_product


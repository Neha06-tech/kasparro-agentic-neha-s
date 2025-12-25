from data.product_input import product_data
from agents.product_parser_agent import ProductParserAgent

parser = ProductParserAgent()
parsed_product = parser.run(product_data)

print(parsed_product)


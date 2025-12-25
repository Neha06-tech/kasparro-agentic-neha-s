from data.product_input import product_data
from agents.product_parser_agent import ProductParserAgent
from logic_blocks.benefits_block import generate_benefits_block
from logic_blocks.usage_block import generate_usage_block

parser = ProductParserAgent()
product = parser.run(product_data)

print(generate_benefits_block(product))
print(generate_usage_block(product))


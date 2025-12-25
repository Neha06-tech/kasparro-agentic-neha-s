from data.product_input import product_data
from agents.product_parser_agent import ProductParserAgent
from agents.question_generator_agent import QuestionGeneratorAgent

parser = ProductParserAgent()
question_agent = QuestionGeneratorAgent()

parsed_product = parser.run(product_data)
questions = question_agent.run(parsed_product)

for category, qs in questions.items():
    print(category, "->", len(qs))


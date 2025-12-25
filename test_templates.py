from data.product_input import product_data
from agents.product_parser_agent import ProductParserAgent
from agents.question_generator_agent import QuestionGeneratorAgent
from templates.faq_template import build_faq_template
from templates.product_template import build_product_template

parser = ProductParserAgent()
question_agent = QuestionGeneratorAgent()

product = parser.run(product_data)
questions = question_agent.run(product)

print(build_faq_template(product, questions))
print(build_product_template(product))


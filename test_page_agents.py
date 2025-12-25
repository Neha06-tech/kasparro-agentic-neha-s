from data.product_input import product_data
from agents.product_parser_agent import ProductParserAgent
from agents.question_generator_agent import QuestionGeneratorAgent
from agents.faq_page_agent import FAQPageAgent
from agents.product_page_agent import ProductPageAgent
from agents.comparison_page_agent import ComparisonPageAgent

parser = ProductParserAgent()
question_agent = QuestionGeneratorAgent()

product = parser.run(product_data)
questions = question_agent.run(product)

faq_agent = FAQPageAgent()
product_agent = ProductPageAgent()
comparison_agent = ComparisonPageAgent()

print(faq_agent.run(product, questions))
print(product_agent.run(product))
print(comparison_agent.run(product))


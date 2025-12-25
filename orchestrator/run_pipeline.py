import json
from data.product_input import product_data
from agents.product_parser_agent import ProductParserAgent
from agents.question_generator_agent import QuestionGeneratorAgent
from agents.faq_page_agent import FAQPageAgent
from agents.product_page_agent import ProductPageAgent
from agents.comparison_page_agent import ComparisonPageAgent

# Initialize agents
parser = ProductParserAgent()
question_agent = QuestionGeneratorAgent()
faq_agent = FAQPageAgent()
product_agent = ProductPageAgent()
comparison_agent = ComparisonPageAgent()

# Step 1: Parse product
product = parser.run(product_data)

# Step 2: Generate questions
questions = question_agent.run(product)

# Step 3: Assemble pages
faq_page = faq_agent.run(product, questions)
product_page = product_agent.run(product)
comparison_page = comparison_agent.run(product)

# Step 4: Save JSON outputs
with open("outputs/faq.json", "w") as f:
    json.dump(faq_page, f, indent=4)

with open("outputs/product_page.json", "w") as f:
    json.dump(product_page, f, indent=4)

with open("outputs/comparison_page.json", "w") as f:
    json.dump(comparison_page, f, indent=4)

print("Pipeline executed successfully! JSON files generated in outputs/")


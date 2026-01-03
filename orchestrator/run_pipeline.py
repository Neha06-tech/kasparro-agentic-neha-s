import json
from agents.product_parser_agent import ProductParserAgent
from agents.question_generator_agent import QuestionGeneratorAgent
from agents.faq_page_agent import FAQPageAgent
from agents.product_page_agent import ProductPageAgent
from agents.comparison_page_agent import ComparisonPageAgent

class SharedState:
    """Shared state for all agents to read/write"""
    def __init__(self):
        self.data = {"pages": {}}

def run_pipeline():
    state = SharedState()

    # Instantiate all agents in execution order
    agents = [
        ProductParserAgent(),
        QuestionGeneratorAgent(),
        FAQPageAgent(),
        ProductPageAgent(),
        ComparisonPageAgent()
    ]

    # Execute agents in sequence, only if can_run() returns True
    for agent in agents:
        if agent.can_run(state):
            agent.run(state)

    # Save JSON outputs to files
    pages = state.data.get("pages", {})
    for page_name, page_content in pages.items():
        filename = f"outputs/{page_name}.json"
        with open(filename, "w") as f:
            json.dump(page_content, f, indent=2)
        print(f"{page_name.capitalize()} page saved to {filename}")

if __name__ == "__main__":
    run_pipeline()


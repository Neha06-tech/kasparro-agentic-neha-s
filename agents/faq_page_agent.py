from agents.base_agent import BaseAgent
from templates.faq_template import build_faq_template

class FAQPageAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="FAQPageAgent")

    def can_run(self, state):
        return hasattr(state, "parsed_product") and hasattr(state, "questions") and not hasattr(state, "faq_page")

    def run(self, state):
        product = state.parsed_product
        questions = state.questions
        faq_page = build_faq_template(product, questions)

        if not hasattr(state, "data"):
            state.data = {"pages": {}}
        state.data["pages"]["faq"] = faq_page

        print("FAQPageAgent: FAQ page added to state.")


from agents.base_agent import BaseAgent
from templates.faq_template import build_faq_template

class FAQPageAgent(BaseAgent):
    """
    Agent responsible for assembling the FAQ page.
    """

    def run(self, product, questions):
        return {
            "page_type": "FAQ",
            "content": build_faq_template(product, questions)
        }


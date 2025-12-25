from agents.base_agent import BaseAgent

class QuestionGeneratorAgent(BaseAgent):
    """
    Agent responsible for generating categorized
    user questions based on product attributes.
    """

    def run(self, product):
        questions = {
            "informational": [
                f"What is {product['name']}?",
                f"What does {product['concentration']} mean?",
                "What skin types is this product suitable for?",
                "What are the key ingredients?",
                "What benefits does this product provide?"
            ],
            "usage": [
                "How should I apply this product?",
                "When is the best time to use this product?",
                "Can this product be used daily?",
                "Should sunscreen be applied after using this product?"
            ],
            "safety": [
                "Is this product safe for sensitive skin?",
                "Are there any side effects?",
                "What should I do if irritation occurs?"
            ],
            "purchase": [
                "What is the price of this product?",
                "Is this product worth the price?"
            ],
            "comparison": [
                "How does this product compare to other vitamin C serums?"
            ]
        }

        return questions


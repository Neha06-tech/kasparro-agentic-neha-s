from agents.base_agent import BaseAgent

class QuestionGeneratorAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="QuestionGeneratorAgent")

    def can_run(self, state):
        return hasattr(state, "parsed_product") and not hasattr(state, "questions")

    def run(self, state):
        product = state.parsed_product
        questions = [
            f"What is {product.get('Product Name', 'this product')}?",
            f"What are the key ingredients in {product.get('Product Name', 'this product')}?",
            f"How should {product.get('Product Name', 'this product')} be used?",
            f"What benefits does {product.get('Product Name', 'this product')} provide?",
            f"Are there any side effects of {product.get('Product Name', 'this product')}?"
        ]
        state.questions = questions
        print("QuestionGeneratorAgent: Questions added to state.")


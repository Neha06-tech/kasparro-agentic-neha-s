Kasparro AI Agentic Content Generation System
Problem Statement
The goal of this project is to design a multi-agent system that can autonomously generate structured content pages for products. The system should demonstrate independent agent responsibilities, dynamic coordination, and produce machine-readable outputs in JSON format.
Solution Overview
This system uses a true agentic architecture where each agent performs a specific role:
ProductParserAgent – Parses raw product data into a structured format.
QuestionGeneratorAgent – Generates relevant questions for the parsed product.
FAQPageAgent – Builds a FAQ page from the generated questions.
ProductPageAgent – Builds a product page using parsed data, usage instructions, and benefits.
ComparisonPageAgent – Compares two products and generates a structured comparison page.
The agents communicate via a shared state managed by an orchestrator, enabling autonomous decision-making without hidden global states.
Scopes & Assumptions
Product data is provided in a consistent structure (product_data).
The system supports multiple content pages: FAQ, product, and comparison.
Each agent executes only when its preconditions are met (checked via can_run).
Outputs are always machine-readable JSON.
The system assumes Ingredients, usage, and benefits keys exist in product data.
System Design
Agent Architecture
Each agent extends BaseAgent and implements:
can_run(state) → Determines if the agent should execute.
run(state) → Executes the agent logic and updates the shared state.
Agents operate modularly, independently, and follow clear boundaries.
Orchestration
Orchestrator maintains a shared state object.
Executes agents sequentially but based on can_run conditions, enabling dynamic control flow.
This ensures agents run only when their dependencies are satisfied.
Reusable Logic Blocks
generate_usage_block – Extracts usage instructions.
generate_benefits_block – Extracts product benefits.
compare_ingredients_block – Compares ingredients across products.
Template Engine
Each content page uses a dedicated template function:
build_faq_template(product, questions)
build_product_template(product, usage, benefits)
build_comparison_template(product_a, product_b)
Templates define fields, rules, and formatting for structured JSON output.
Machine-Readable Output
All final pages are saved in JSON format:
outputs/faq.json
outputs/product.json
outputs/comparison.json
Flow Diagram
ProductParserAgent --> QuestionGeneratorAgent --> FAQPageAgent
                  \
                   --> ProductPageAgent --> ComparisonPageAgent
Flowchart of Agent Execution
+-------------------+
| ProductParserAgent|
+-------------------+
           |
           v
+-----------------------+
| QuestionGeneratorAgent|
+-----------------------+
           |
           v
+-------------------+
|   FAQPageAgent    |
+-------------------+

ProductParserAgent also triggers:

           |
           v
+-------------------+
| ProductPageAgent  |
+-------------------+
           |
           v
+------------------------+
| ComparisonPageAgent    |
+------------------------+


Template Structure


FAQ Template:
{
  "product": "Product Name",
  "faqs": [
    {
      "category": "Category Name",
      "question": "Sample question?",
      "answer": "Sample answer related to product."
    },
    ...
  ]
}

Product Template:
{
  "name": "Product Name",
  "description": "Product description",
  "usage": "How to use instructions",
  "benefits": ["Benefit 1", "Benefit 2"]
}

Comparison Template:
{
  "product_a": "Product A Name",
  "product_b": "Product B Name",
  "common_ingredients": ["Ingredient 1", "Ingredient 2"],
  "unique_to_product_a": ["Ingredient X"],
  "unique_to_product_b": ["Ingredient Y"]
}


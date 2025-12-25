from logic_blocks.benefits_block import generate_benefits_block
from logic_blocks.usage_block import generate_usage_block
from logic_blocks.safety_block import generate_safety_block
from logic_blocks.pricing_block import generate_pricing_block

def build_product_template(product):
    page = {
        "name": product["name"],
        "concentration": product["concentration"],
        "skin_type": product["skin_type"],
        "ingredients": product["ingredients"]
    }

    page.update(generate_benefits_block(product))
    page.update(generate_usage_block(product))
    page.update(generate_safety_block(product))
    page.update(generate_pricing_block(product))

    return page


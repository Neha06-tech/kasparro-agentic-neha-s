def generate_benefits_block(product):
    return {
        "benefits": product.get("benefits", ["No benefits information available."])
    }


def generate_usage_block(product):
    return {
        "how_to_use": product.get("how_to_use", "Usage instructions not available."),
        "duration": product.get("duration", "Duration info not available."),
    }


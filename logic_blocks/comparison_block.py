def compare_ingredients_block(product_a, product_b):
    return {
        "common_ingredients": list(set(product_a.get("Ingredients", [])) & set(product_b.get("Ingredients", []))),
        "unique_to_product_a": list(set(product_a.get("Ingredients", [])) - set(product_b.get("Ingredients", []))),
        "unique_to_product_b": list(set(product_b.get("Ingredients", [])) - set(product_a.get("Ingredients", []))),
    }


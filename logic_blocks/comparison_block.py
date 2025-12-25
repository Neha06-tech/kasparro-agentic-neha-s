def compare_products(product_a, product_b):
    return {
        "product_a": {
            "name": product_a["name"],
            "ingredients": product_a["ingredients"],
            "benefits": product_a["benefits"],
            "price": product_a["price"]
        },
        "product_b": product_b
    }


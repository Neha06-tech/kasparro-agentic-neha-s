def build_comparison_template(product_a, product_b, comparison=None):
    return {
        "product_a": product_a.get("Product Name", "Unknown"),
        "product_b": product_b.get("Product Name", "Unknown"),
        "comparison": comparison or {}
    }


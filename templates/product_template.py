def build_product_template(product, usage=None, benefits=None):
    return {
        "name": product.get("Product Name", "Unknown"),
        "description": product.get("Description", ""),
        "usage": usage or {},
        "benefits": benefits or {}
    }


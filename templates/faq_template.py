def build_faq_template(product, questions):
    faq_items = []
    count = 0
    for q in questions:
        if count >= 5:
            break
        faq_items.append({
            "question": q,
            "answer": f"This information is related to {product.get('Product Name', 'the product')}."
        })
        count += 1

    return {
        "product": product.get("Product Name", "Unknown"),
        "faqs": faq_items
    }


def build_faq_template(product, questions):
    faq_items = []

    count = 0
    for category, qs in questions.items():
        for q in qs:
            if count >= 5:
                break
            faq_items.append({
                "category": category,
                "question": q,
                "answer": f"This information is related to {product['name']}."
            })
            count += 1

    return {
        "product": product["name"],
        "faqs": faq_items
    }


def validate_amount(order):
    if "amount" not in order:
        return None, f"missing amount: {order}"

    amount = order["amount"]

    if not isinstance(amount, (int, float)):
        return None, f"non-numeric amount: {order}"

    if amount < 0:
        return None, f"amount cannot be negative: {order}"

    return float(amount), None


def calculate_amount(amount, customer_country):
    if customer_country == "PL":
        amount *= 1.23
    elif customer_country == "DE":
        amount *= 1.19

    discount = 0
    is_high_value = False

    if amount > 1000:
        discount = amount * 0.1
        amount *= 0.9
        is_high_value = True

    return amount, discount, is_high_value


def process_orders(orders, customer_country):
    total = 0
    discount_total = 0
    high_value_count = 0
    errors = []

    for order in orders:
        amount, error = validate_amount(order)

        if error:
            errors.append(error)
            continue

        amount, discount, is_high_value = calculate_amount(amount, customer_country)

        total += amount
        discount_total += discount

        if is_high_value:
            high_value_count += 1

    return {
        "total": total,
        "discount_total": discount_total,
        "high_value_count": high_value_count,
        "errors": errors,
    }
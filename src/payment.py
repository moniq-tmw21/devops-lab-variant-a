from decimal import Decimal, ROUND_HALF_UP


def calculate_total(price, quantity):
    """Return an exact, two-decimal payment total."""
    value = Decimal(str(price))
    if not value.is_finite() or value < 0:
        raise ValueError("price must be finite and non-negative")
    if isinstance(quantity, bool) or not isinstance(quantity, int) or quantity < 1:
        raise ValueError("quantity must be a positive integer")
    return (value + quantity).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

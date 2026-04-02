def place_order(order_id: int, order_amount: float) -> None:
    if is_order_invalid(order_id):
        show_invalid_order_message()
        return

    final_amount = calculate_final_amount(order_amount)
    persist_order(order_id, final_amount)
    show_order_success_message()


def is_order_invalid(order_id: int) -> bool:
    return order_id <= 0


def calculate_final_amount(order_amount: float) -> float:
    discount = calculate_discount(order_amount)
    tax = calculate_tax(order_amount)
    return (order_amount + tax) - discount


def calculate_discount(amount: float) -> float:
    return amount * 0.10


def calculate_tax(amount: float) -> float:
    return amount * 0.18


def persist_order(order_id: int, amount: float) -> None:
    print("Order saved in database")


def show_invalid_order_message() -> None:
    print("Order cannot be empty")


def show_order_success_message() -> None:
    print("Order placed successfully")

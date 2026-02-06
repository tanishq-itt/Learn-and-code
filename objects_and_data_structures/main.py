from paperboy import Paperboy
from customer import Customer
from wallet import Wallet


def main():
    wallet = Wallet(balance=50.0)
    customer = Customer("Tanishq", "M", wallet)
    paperboy = Paperboy()

    payment_successful = paperboy.collect_payment(customer, 50.0)

    if payment_successful:
        print("Payment collected successfully.")
    else:
        print("Customer could not pay. Come back later.")


if __name__ == "__main__":
    main()

class Paperboy:
    def collect_payment(self, customer, amount):
        
        if customer.pay(amount):
            return True

        return False

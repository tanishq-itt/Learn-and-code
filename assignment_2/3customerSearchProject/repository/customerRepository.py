class CustomerRepository:
    def __init__(self, customers):
        self.customers = customers

    def get_all(self):
        return self.customers

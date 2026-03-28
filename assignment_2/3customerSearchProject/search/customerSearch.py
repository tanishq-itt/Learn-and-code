class CustomerSearch:
    def __init__(self, repository):
        self.repository = repository

    def search(self, value, field):
        matched = []
        for customer in self.repository.get_all():
            if value in getattr(customer, field):
                matched.append(customer)

        return sorted(matched, key=lambda c: c.customerId)

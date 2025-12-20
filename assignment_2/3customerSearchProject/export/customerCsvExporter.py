class CustomerCsvExporter:
    def export(self, customers):
        lines = []
        for customer in customers:
            lines.append(
                f"{customer.customerId},"
                f"{customer.companyName},"
                f"{customer.contactName},"
                f"{customer.country}"
            )

        return "\n".join(lines)

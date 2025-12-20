from repository.customerRepository import CustomerRepository
from search.customerSearch import CustomerSearch
from export.customerCsvExporter import CustomerCsvExporter

repo = CustomerRepository(db.customers)
search = CustomerSearch(repo)
exporter = CustomerCsvExporter()
customers = search.search("India", "country")
csv_data = exporter.export(customers)

print(csv_data)

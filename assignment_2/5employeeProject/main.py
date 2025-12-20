from employee import Employee
from addEmployee import AddEmployee
from reports.csvReport import EmployeeReportCSV
from reports.xmlReport import EmployeeReportXML
from services.terminateEmployee import EmployeeService

employee = Employee(1, "Tanishq", "Engineering")

repository = AddEmployee()
repository.save(employee)

csv_report = EmployeeReportCSV()
csv_report.generate(employee)

xml_report = EmployeeReportXML()
xml_report.generate(employee)

service = EmployeeService()
service.terminate(employee)

print("Is working:", employee.is_working())

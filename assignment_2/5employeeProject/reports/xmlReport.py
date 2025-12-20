from reports.report import EmployeeReport

class EmployeeReportXML(EmployeeReport):
    def generate(self, employee):
        print("XML Report:")
        print(
            f"<employee>"
            f"<id>{employee.emp_id}</id>"
            f"<name>{employee.name}</name>"
            f"<department>{employee.department}</department>"
            f"</employee>"
        )

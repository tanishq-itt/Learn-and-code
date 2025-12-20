from reports.report import EmployeeReport

class EmployeeReportCSV(EmployeeReport):
    def generate(self, employee):
        print("CSV Report:")
        print(f"{employee.emp_id},{employee.name},{employee.department}")

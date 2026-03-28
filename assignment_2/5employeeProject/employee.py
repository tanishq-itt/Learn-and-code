class Employee:
    def __init__(self, emp_id, name, department, working):
        self.id = emp_id
        self.name = name
        self.department = department
        self.working = working

    def save_employee_to_database(self):
        print("Saving employee to database")

    def print_employee_detail_report_xml(self):
        print("Printing employee report in XML")

    def print_employee_detail_report_csv(self):
        print("Printing employee report in CSV")

    def terminate_employee(self):
        self.working = False

    def is_working(self):
        return self.working

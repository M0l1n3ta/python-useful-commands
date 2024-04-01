from Employee import Employee

class Manager(Employee):

    def get_info(self):
        return f"Manager {self.get_full_name()}, salary {self.salary}"

employees = [
    Manager("Vera","Strokes", 2000),
    Employee("Chuck","Chung", 1800),
    Employee("Dave","Smith", 1900),
]

for e in employees:
    print(e.get_info())
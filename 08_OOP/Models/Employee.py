class Employee:  
	def __init__(self, first_name, last_name, salary):  
		self.first_name = first_name  
		self.last_name = last_name  
		self.salary = salary
		
	def get_full_name(self):  
		return f"{self.first_name} {self.last_name}"	

	def get_info(self):
		return f"Employee {self.get_full_name()}, salary {self.salary}"
	
	
		
e1 = Employee("Vera", "Schmidt", 2000)  
e2 = Employee("Chuck", "Murphy", 1800)  
e3 = Employee("Dave", "Dreissing", 1900)  
  
print(e1.get_full_name())  
print(e2.get_full_name())  
print(e3.get_info())
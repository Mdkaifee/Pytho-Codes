class Employee:
    def __init__(self,name,age,salary,gender):
        self.name=name
        self.age=age
        self.salary=salary
        self.gender=gender
    def show_employee_details(self):
         print("Name of employee:",self.name)
         print("Age:",self.age)
         print("salary:",self.salary)
         print("gender:",self.gender)

e1=Employee('SAM',32,85000,'Male')
e1.show_employee_details()

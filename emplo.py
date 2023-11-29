class Employee:
        def __init__(self, emp_id, emp_name, emp_salary, emp_department):
            self.emp_id= emp_id
            self.emp_name= emp_name
            self.emp_salary= emp_salary
            self.emp_department= emp_department
        
            def calculate_emp_salary(self):
            #self.emp_salary
            #self.hours_worked
            print("salary".format(self.emp_salary))
            overtime=0
           if hours_worked > 50:
                  overtime= emp_salary - 50
                    return "overtime{} =".format(self.hours_worked)
        # def emp_assign_department(self, emp_department):

            
        #def print_employee_details(self, emp_name, emp_id,emp_salary, emp_department):
            
        def print_employee_details(self):
            return"nam{} id {} salary {} department".format(self.emp_name,self.emp_id, self.emp_salary, self.emp_department)
emp1= Employee("aaa", 123, 100, "Mar")
print(emp1)
'''
Created on Aug 30, 2016

@author: alokkumar
'''
class Employee:
    empCount = 0
    def __init__(self, name, salary):
        self.name= name
        self.salary= salary
        Employee.empCount +=1
    
    def displayCount(self):
        print("Total employees=", emp1.empCount)
    def displayEmployees(self):
        print("Name : ", self.name,  ", Salary: ", self.salary)          

emp1 = Employee("alok" ,1000)
emp1.displayCount() 
emp1.displayEmployees() 
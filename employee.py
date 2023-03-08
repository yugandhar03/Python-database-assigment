from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, id, name,email, salary):
        # id is defined as Protected 
        self._id= id
        # name & email is defined as a Public
        self.name = name
        self.email=email
        # salary is defined as Private
        self.salary = salary

    def get_name(self):
        return self.name

    def get_salary(self):
        return self.__salary

    @abstractmethod
    def display(self):
       pass

# Instance creation:-
# emp=Employee(1,"Bob Johnson","bob@gmail.com", 80000)

# Public:-
# print(emp.name)
# print(emp.email)
# output:- Bob Johnson,bob@gmail.com

# Protected:-
# print(emp._id)
# output:- 1

# Private
# print(emp.__salary)
# output:- Employee' object has no attribute '__salary'
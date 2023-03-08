from database import get_database_connection
from employee import Employee
from permanent_employee import PermanentEmployee
from contract_employee import ContractEmployee

db = get_database_connection()
collection = db['employee']

class EmployeeManagement:
    def __init__(self):
        self.employee_docs = []
       
    def add_employee(self, employee):
       # create a list of employee documents to insert
       for contract_employee in employee:
            employee_doc = {
                "emp_id": contract_employee._id,
                "name": contract_employee.name,
                "email": contract_employee.email,
                "salary": contract_employee.salary,
            }
            if isinstance(employee, ContractEmployee):
             employee_doc["contract_period"] = employee.contract_period
             employee_doc["hourly_rate"] = employee.hourly_rate
            elif isinstance(employee, PermanentEmployee):
                employee_doc["notice_period"] = employee.notice_period
                employee_doc["gratuity_amount"] = employee.gratuity_amount
            self.employee_docs.append(employee_doc)

       result = collection.insert_many(self.employee_docs)
       print(result.inserted_ids)
       
    def remove_employee(self, id):
        # remove the employee record
        result = collection.delete_one({"emp_id":id})
        # print the result
        print(result.deleted_count, "employee record deleted")

    def search_employee(self, email):
        # find one employee record
        result = collection.find({"email":email})
        for employee in result:
            print(employee)

    def display_all_employees(self):
        # find one employee record
        result = collection.find({})
        for employee in result:
            print(employee)


management = EmployeeManagement()

# add employees
# create a list of ContractEmployee objects
contract_employees = [
    ContractEmployee(1, "John", "john@gmail.com", 50000, 6, 4000),
    ContractEmployee(2, "Hari", "hari@gmail.com", 60000, 7, 5000),
    ContractEmployee(3, "Mike", "mike@gmail.com", 70000, 8, 6000),
    PermanentEmployee(10, "John", "john@gmail.com", 50000, 6, 4000),
    PermanentEmployee(20, "Hari", "hari@gmail.com", 60000, 7, 5000),
    PermanentEmployee(30, "Mike", "mike@gmail.com", 70000, 8, 6000)
]

# #add an employee
# management.add_employee(contract_employees)

# #Search an employee
management.search_employee("john@gmail.com")

# #remove an employee
# management.remove_employee(1)

# #display all employees again
# management.display_all_employees()
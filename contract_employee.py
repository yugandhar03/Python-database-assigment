from employee import Employee

class ContractEmployee(Employee):
    def __init__(self, id, name, email, salary, contract_period, hourly_rate):
        super().__init__(id, name, email, salary)
        self.contract_period = contract_period
        self.hourly_rate = hourly_rate
    
    def display(self):
        return {"Name":self.name,"Email":self.email,"salary":self.salary, "contract_period":self.contract_period,"hourly_rate":self.hourly_rate}
        # print(f"id:{self._id},Name:{self.name},Email:{self.email}, contract_period:{self.contract_period},hourly_rate:{self.hourly_rate}")

    
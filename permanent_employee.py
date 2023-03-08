from employee import Employee

class PermanentEmployee(Employee):
    def __init__(self, id, name, email, salary, notice_period, gratuity_amount):
        super().__init__(id, name, email, salary)
        self.notice_period = notice_period
        self.gratuity_amount = gratuity_amount
    
    def display(self):
        return {"Name":self.name,"Email":self.email, "salary":self.salary,"contract_period":self.notice_period,"gratuity_amount":self.gratuity_amount}
        # print(f"id:{self._id},Name:{self.name},Email:{self.email}, contract_period:{self.notice_period},hourly_rate:{self.gratuity_amount}")

    

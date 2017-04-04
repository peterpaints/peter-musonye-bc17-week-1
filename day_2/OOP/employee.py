class Employee(object):
    def __init__(self, name, payroll_number, experience_level='junior'):
        self.name = name
        self.payroll_number = payroll_number
        self.experience_level = 'junior' if experience_level is None else experience_level
        self.hourly_rate = 30 if experience_level == 'junior' else 60 if experience_level == 'mid_level' else 100

    def gross_pay(self, hours_worked=160):
        self.hours_worked = hours_worked
        self.hours_worked = 160 if hours_worked is None else hours_worked
        return hours_worked * self.hourly_rate

    def net_pay(self, tax_bracket=0):
        gross = self.gross_pay()
        self.tax_bracket = tax_bracket
        tax_bracket = 0.2 if self.hourly_rate < 60 else 0.3 if self.hourly_rate == 60 else 0.4
        return gross - (tax_bracket * gross)


class Manager(Employee):
    def __init__(self, name, payroll_number, experience_level='junior'):
        self.name = name
        self.payroll_number = payroll_number
        self.experience_level = 'junior' if experience_level is None else experience_level
        self.hourly_rate = 60 if experience_level == 'junior' else 120 if experience_level == 'mid_level' else 200


Recruitment_Manager = Manager('Zipporah', '123456', 'mid_level')

print Recruitment_Manager.net_pay()

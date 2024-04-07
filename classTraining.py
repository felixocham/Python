class Employee:
    num_of_employees = 0
    raise_amount = 1.04

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = f"{last.lower()}.{first.lower()}@company.com"

        Employee.num_of_employees += 1

    def full_name(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        return int(self.salary) * self.raise_amount

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, salary = emp_str.split("-")
        return cls(first, last, salary)


emp_1 = Employee("Felix", "Onyango", 60000)
emp_2 = Employee("Larry", "Tester", 70000)
emp_3 = Employee("Fred", "Peter", 85000)
print(emp_1.email)
print(emp_2.email)

print("{} {}".format(emp_1.first, emp_1.last))
print(emp_1.full_name())

print(emp_1.salary)
print(emp_1.apply_raise())

print(Employee.num_of_employees)

Employee.set_raise_amount(1.06)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

emp_str_1 = "John-Doe-70000"
emp_str_2 = "Steve-Smith-30000"
emp_str_3 = "jane-Doe-90000"

new_emp_1 = Employee.from_string(emp_str_1)
new_emp_2 = Employee.from_string(emp_str_2)
new_emp_3 = Employee.from_string(emp_str_3)

print(new_emp_1.email)
print(new_emp_1.salary)
print(new_emp_1.apply_raise())

print(new_emp_2.email)
print(new_emp_2.salary)
print(new_emp_2.apply_raise())

print(Employee.num_of_employees)

class Person:
    def __init__(self, name, age, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} ({self.age})'


class Employee(Person):
    def __init__(self, name, age, salary, dept, **kwargs):
        super().__init__(name, age, **kwargs)
        self.salary = salary
        self.dept = dept

    def __str__(self):
        return f'{Person.__str__(self)} Sal: {self.salary} Dept: {self.dept}'


class Commissioned:
    def __init__(self, rate, **kwargs):
        super().__init__()
        self.comm_rate = rate

    def __str__(self):
        return f'Rt: {self.comm_rate}'


class Salesperson(Employee, Commissioned):
    def __init__(self, name, age, salary, region, dept='Sales', rate=0.02):
        super().__init__(name=name, age=age, salary=salary, dept=dept, rate=rate)
        self.region = region

    def __str__(self):
        emp_str = Employee.__str__(self)
        comm_str = Commissioned.__str__(self)
        return f'{emp_str}, {comm_str} - Reg: {self.region}'


s = Salesperson('William', 37, 99275.00, 'Northeast')
print(s)
print(Salesperson.mro())

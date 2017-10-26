class Employee:
    """docstring forEmployee."""
    num_of_emps = 0
    raise_amt = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_of_emps += 1

    @property  # Convert methods to attributes
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):  # representation object
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)  # re-create object

    def __str__(self): # readable representation object
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other): # '+'
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

    @classmethod
    def set_raise_amt(cls, amount):  #cls just like 'self' of class
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workdate(day):
        if day.weekday() >= 5:
            return False
        return True

class Developer(Employee): # Inheritance Employee
    raise_amt = 1.10
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

emp01 = Employee('Yuan', 'Chun', 48000)
emp02 = Employee('Yi', 'Ray', 38000)
dev01 = Developer('Baal', 'Wu', 50000, 'Python')
dev02 = Developer('Nico', 'Liang', 40000, 'Java')
mgr01 = Manager('Cory', 'Ke', 90000, [dev01, dev02])

emp01.fullname = 'Jin Joa'

print(emp01.email)

del emp01.fullname
print(emp01.email)

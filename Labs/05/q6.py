#Programmer: Amna(23k-0066)
#Date: 18th Sept 2024

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        pass


class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def calculate_bonus(self):
        self.bonus = self.salary * (20/100)
        return self.bonus

    def hire(self):
        print("Manager is hiring")

class developer(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def calculate_bonus(self):
        self.bonus = self.salary * (10/100)
        return self.bonus

    def write_code(self):
        print("Developer is coding...")


class seniorManager(Manager):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def calculate_bonus(self):
        self.bonus = self.salary * (30/100)
        return self.bonus


b = Manager("Alice", 45000)
bonus1 = b.calculate_bonus()
print("Bonus of manager: ", bonus1)

c = developer("Charles", 35000)
bonus2 = c.calculate_bonus()
print("Bonus of developer: ", bonus2)

d = seniorManager("David", 657000)
bonus3 = d.calculate_bonus()
print("Bonus of senior manager: ", bonus3)

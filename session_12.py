class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Tạo một đối tượng và hiển thị thông tin
person1 = Person("Alice", 25)
person1.display_info()

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car: {self.brand} {self.model}, Year: {self.year}")

# Tạo một đối tượng và hiển thị thông tin
car1 = Car("Toyota", "Camry", 2022)
car1.display_info()

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

# Tạo đối tượng và kiểm tra các phương thức
rect = Rectangle(5, 10)
print(f"Diện tích: {rect.get_area()}")
print(f"Chu vi: {rect.get_perimeter()}")

class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Đã gửi {amount}. Số dư mới: {self.balance}")
        else:
            print("Số tiền gửi phải lớn hơn 0.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Đã rút {amount}. Số dư còn lại: {self.balance}")
        else:
            print("Số tiền rút không hợp lệ hoặc không đủ số dư.")

    def display_balance(self):
        print(f"Số dư tài khoản {self.account_number}: {self.balance}")

# Lớp SavingsAccount kế thừa từ BankAccount
class SavingsAccount(BankAccount):
    def __init__(self, account_number, owner, balance=0, interest_rate=0.02):
        super().__init__(account_number, owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Lãi suất đã được áp dụng. Số dư mới: {self.balance}")

# Tạo đối tượng và kiểm tra các phương thức
acc1 = SavingsAccount("123456", "Bob", 1000, 0.05)
acc1.display_balance()
acc1.deposit(500)
acc1.withdraw(300)
acc1.apply_interest()

class Employee:
    def __init__(self, name, salary, position):
        self.name = name
        self.salary = salary
        self.position = position

    def display_info(self):
        print(f"Employee: {self.name}, Position: {self.position}, Salary: {self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, position, team=None):
        super().__init__(name, salary, position)
        self.team = team if team else []

    def add_employee(self, employee):
        self.team.append(employee)
        print(f"{employee.name} has been added to {self.name}'s team.")

    def display_team(self):
        print(f"{self.name}'s team:")
        for emp in self.team:
            emp.display_info()

# Tạo đối tượng và kiểm tra các phương thức
emp1 = Employee("Alice", 50000, "Developer")
emp2 = Employee("Bob", 55000, "Designer")

manager = Manager("Charlie", 70000, "Project Manager")
manager.add_employee(emp1)
manager.add_employee(emp2)

manager.display_team()
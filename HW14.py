# N1

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says: Woof!")

    def info(self):
        print(f"Name: {self.name}, Age: {self.age}")


# N2


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height

# N3


class BankAccount:
    bank_name = "Step Bank"

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount

    def show_balance(self):
        print(f"Bank: {self.bank_name}, Owner: {self.owner}, Balance: {self.balance}")     

# N4


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def average(self):
        if not self.students:
            return 0.0
        total_grades = sum(student.grade for student in self.students)
        return round(total_grades / len(self.students), 2)

    def top_student(self):
        if not self.students:
            return None
        best = max(self.students, key=lambda s: s.grade)
        return best.name
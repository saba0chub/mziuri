class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("aige sesxi martivad")
        else:
            self.balance -= amount
            print("tqven warmatebit gamoitanet tanxa(martla ara ogond)")


    def deposit(self, amount):
        if amount > 2500:
            print("raambavia ")
        else:
            self.balance += amount
            print("tqven warmatebit shoeitanet tanxa")

    def display_balance(self):
        print(self.balance)



bank = BankAccount("kaci", 2500)
bank.withdraw(100)
bank.display_balance()
bank.deposit(400)
bank.display_balance()
bank.withdraw(7800)
bank.deposit(2501)

#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

from math import sqrt

class Shape:
    def describe(self):
        print("I am a shape")


class Polygon(Shape):
    def __init__(self, *args):
        pass

class Triangle(Polygon):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calculate_area(self):
        s = (self.a + self.b + self.c) / 2
        fartobi = float(sqrt(s*(s-self.a)*(s-self.b)*(s-self.c)))

        print("fartobi = ", fartobi)


shape = Shape()
shape.describe()

triangle = Triangle(5, 6, 7)
triangle.calculate_area()
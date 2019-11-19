# This is 
class Student:
    name = "Nick"
    age = 28

    def introduce(self):
        print("My name is " + self.name)
        print("I am " + str(self.age) + " old")


s1 = Student()
s1.introduce()
print(s1)


# __init__ method

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("My name is " + self.name)
        print("I am " + str(self.age) + " old")


s1 = Student("nick", 28)
s1.introduce()
print(s1)


class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y


r = Rectangle(4, 5)
r.area()
print(r)


# __new__ method
class CString(str):
    def __new__(cls, string):
        string = string.upper()
        return str.__new__(cls, string)


a = CString("my name is nick")
print(a)


class Calculator(int):
    def __add__(self, other):
        return int.__sub__(self, other)

    def __sub__(self, other):
        return int.__add__(self, other)


c = Calculator(5)
b = Calculator(3)
print(c + b)


# __radd__ inverse operation
class Radd(int):
    def __radd__(self, other):
        return int.__sub__(self, other)


r = Radd(6)
b = Radd(-5)
print(r+b)
# b assign to self
print(1+b)


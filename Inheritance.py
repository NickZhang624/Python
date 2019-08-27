import random as r

class Parent:
    def hello(self):
        print("this is parent class")


class Child(Parent):
    pass


p = Parent()
p.hello()
c = Child()
c.hello()


# if child class has same function with parent class,
# the function in child class will override


class Child(Parent):
    def hello(self):
        print("This is child class")


c = Child()
c.hello()
print("-------------------------------------")


class Fish:
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)

    def move(self):
        self.x -= 1
        print("My location is ", + self.x, self.y)


class Salmon(Fish):
    pass


class Shark(Fish):
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("I am hungry")
            self.hungry = False
        else:
            print("I am full")


f = Fish()
f.move()
s = Salmon()
s.move()
s = Shark()
s.eat()
s.eat()

# s.move()
# Error: 'Shark' object has no attribute 'x'
# As child class shark has same function, so it will be override, error
print("-----------------------------------------")


# There are two solution to fix this error
# Solution 1
class Fish:
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)

    def move(self):
        self.x -= 1
        print("My location is ", + self.x, self.y)


class Salmon(Fish):
    pass


class Shark(Fish):
    def __init__(self):
        # Just call parent class function, but
        # __init__(self) is child class function method!!!!!
        Fish.__init__(self)
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("I am hungry")
            self.hungry = False
        else:
            print("I am full")


f = Fish()
f.move()
s = Salmon()
s.move()
s = Shark()
s.eat()
s.eat()
s.move()
print("-------------------------------")

# Solution 1
# Super!!!!!!!!!!!!!!!!!!!!!!!
class Fish:
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)

    def move(self):
        self.x -= 1
        print("My location is ", + self.x, self.y)


class Salmon(Fish):
    pass


class Shark(Fish):
    def __init__(self):
        # Super can call parent class function just like below
        # as if there are multiple parent classes, just type in your
        # child class(), not need to modify code below
        super().__init__()
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("I am hungry")
            self.hungry = False
        else:
            print("I am full")


f = Fish()
f.move()
s = Salmon()
s.move()
s = Shark()
s.eat()
s.eat()
s.move()
print("-------------------------")

# Multiple inheritance
class Base1:
    def show1(self):
        print("This is base 1")


class Base2:
    def show2(self):
        print("This is base 2")

class M(Base1, Base2):
    pass


m = M()
m.show1()
m.show2()
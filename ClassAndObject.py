class Nick:
    # variable
    age = 28
    height = 171
    weight = 60
    lastname = "zhang"

    # function
    # self means this
    def c(self):
        print("Nick can create a programme by C")

    def java(self):
        print("Nick can create a grogramme by Java")

    def python(self):
        print("Nick can create a programme by Python")


temp = Nick()
print(temp.age)
temp.python()

# object in class

class Nation:
    def setCountry(self, country):
        self.country = country

    def show(self):
        print("I live in" + self.country)


a = Nation()
a.setCountry("New Zealand")
b = Nation()
b.setCountry("China")

a.show()
b.show()


# private and public

class Person:
    name = "Nick"

p = Person()
print(p.name)


# Change to private just add __ before name
class Person:
    __name = "Zoe"


p = Person()
# print(p.__name)


# this is solution if want to access this variable
class Person:
    __name = "Zhang"

    def getname(self):
        return self.__name


p = Person()
print(p.getname())

# _Class name__private variable
print(p._Person__name)



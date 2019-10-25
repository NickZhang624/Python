# This is eighth part to introduce Python function
# A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.

# In Python a function is defined using the def keyword:
def FirstFunction():
    print("the first function")

FirstFunction()

print(type(FirstFunction))

def sting(name):
    print(name + " zhang")

sting("nick")

def add(num1, num2):
    print(num1 + num2)

add(3,4)

print("-----------------------------------")


# Keyword Parameters
def Name(name, age):
    print("My name is " + name + ", " + str(age) + " years old")

Name("nick" , 23)

Name(age=28, name="Zoe")


# Default parameter value
def Name1(name="Nick", age=24):
    print("My name is " + name + ", " + str(age) + " years old")

Name1()

print("-------------------------------------")


# collect parameters
def test(*par):
    print("The length is: ", len(par))
    print("The second parameter is: ", par[1])

test(1, "nick", 2.3, "!")

def test1(*par, name):
    print("The length is: ", len(par), name)
    print("The second parameter is: ", par[1])

test1(1, "nick", 2.3, "!", name="Athar")

def test1(*par, name="Athar"):
    print("The length is: ", len(par), name)
    print("The second parameter is: ", par[1])

test1(1, "nick", 2.3, "!")

print("-------------------------------------")


# return
def hello():
    print("Hello nick")
hello()

# temp is a return value
temp = hello()
print(temp)

print(type(temp))


# return list
def back():
    return [1, "nick", 3.4]
print(back())


# return tuple
def back1():
    return 1, "Nick", 3.5

print(back1())

print("-------------------------------------")


# local variable and global variable
def discount(price, rate):
    final_price = price * rate
    # here trying to print global variable
    print("global variable: ", old_price)
    return final_price

old_price = float(input("Please enter a price: "))
rate = float(input("Please enter a rate: "))
new_price =discount(old_price, rate)
print("Discount price is: ", new_price)

# can not print "final_price" as it is a local variable

print("-------------------------------------")


# modify global variable value
count = 3
def Cou():
    count = 5
    print(count)
Cou()
print(count)

count = 3
def Cou():
    # modify here
    global count
    count = 5
    print(count)
Cou()
print(count)
print("-------------------------------------")


# internal function
def fun1():
    print("print fun1")
    def fun2():
        print("print fun2")
    fun2()

fun1()

print("---------------------------------------")


# closure
def funx(x):
    def funy(y):
        return x * y
    return funy

i = funx(4)
print(i)
print(type(i))

print(i(10000))

print(funx(5)(6))


# three elements
def funx(x):
    def funy(y):
        def funz(z):
            return x * y * z
        return funz
    return funy

print(funx(3)(4)(5))


# Nonlocal function
def fun3():
    x = 5
    def fun4():
        nonlocal x
        x *= x
        return x
    return fun4()

print(fun3())

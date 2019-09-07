# *args

def add(num1, num2, num3):
    print(num1+num2+num3)

add(1,2,3)


def add(*args):
    print(sum(args))

add(1,2,3)

# Tuple
def add(*args):
    print(type(args))

add(1,2)


def add(*args):
    for i in args:
        print("My name is ", i)

add(1,2)


# **kwargs  key word
# dictionary
def m(*args, **kwargs):
    print(type(args))
    print(type(kwargs))

m(1,2)

dic_pepole = {'name':'nick', 'age':'28'}

for e, r in dic_pepole.items():
    print(e, ":", r)


def m(dic_person):
    for e, r in dic_person.items():
        print(e, ":", r)

m(dic_pepole)


def m(**kwargs):
    for e, r in kwargs.items():
        print(e, ":", r)

m(name='ted', age='18')

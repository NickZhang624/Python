# This is ninth part to introduce Python function
# A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.

# In Python a function is defined using the def keyword:

g = lambda x: 2*x +1

print(g(5))

def add(x, y):
    return x+y
print(add(3,4))

add= lambda x,y:x+y
print(add(3,4))


def func(x):
    return lambda y:y*x

res = func(2)
print(res(11))

print(res(250))

# filter

def odd(x):
    return x%2

temp = range(0,10)
show = filter(odd,temp)
print(list(show))

print(list(filter(lambda x:x%2,range(10))))

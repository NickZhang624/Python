# This is ninth part to introduce Python lambda
# A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression.

g = lambda x: 2*x +1

print(g(5))

# function way to calculate 
def add(x, y):
    return x+y
print(add(3,4))

# lambda way to calculate
add= lambda x,y:x+y
print(add(3,4))

# embedded lambda in function
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

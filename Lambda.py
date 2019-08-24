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

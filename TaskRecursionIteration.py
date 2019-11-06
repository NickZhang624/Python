#This small task uses recursion, iteration in Python programme and a famous sample Tower of Hanoi

# recursion
def rec(n):
    if n == 1:
        return 1
    else:
        return n * rec(n-1)

number = int(input("Plese enter a number: "))
print(rec(number))

# for loop

def rec(n):
    result = n
    for i in range(1, n):
        result *= i

    return result

print(rec(7))


# [1,2,3,4,5,6,7,8,9]
# [1,1,2,3,5,8,13,21,34]

# iteration

def fab(n):
    n1 = 1
    n2 = 1
    n3 = 1

    if n<1:
        print("Error")
        return -1

    while (n-2)>0:
        n3 = n2 + n1
        n1 = n2
        n2 = n3
        n -= 1

    return n3

result = fab(3)
if result != -1:
    print(result)

# recursion
def fab(n):
    if n<1:
        print("error")
        return -1
    if n == 1 or n == 2:
        return 1
    else:
        return fab(n-1) + fab(n-2)

result = fab(3)
if result != -1:
    print(result)

# Tower of Hanoi
def hanoi(n,x,y,z):
    if n == 1:
        print(x, ">" , z)
    else:
        hanoi(n-1,x,z,y)# move n-1 from x to y
        print(x, ">",  z)# move the last one from x to z
        hanoi(n-1,y,x,z)# move n-1 from y to z

n = int(input("Please enter levels of hanoi: "))
hanoi(n, "X", "Y", "Z")


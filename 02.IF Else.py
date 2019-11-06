#This is second part to introduce Python if else/ elif statements

#numerical comparsion using if statements
a = 50
b = 20

if a < b:
    print("wrong")
else:
    print("right")

#This sample introduce if elif statements to implement a score rank by if elif statements
score = input("Please enter your score?")
if 100>= int(score) >=90:
    print("A")
elif 90> int(score) >=80:
    print("B")
elif 80> int(score) >=60:
    print("C")
elif 60> int(score) >=0:
    print("failed")
else:
    print("Please only enter your score number from 0 to 100")


#ohter way to compare the size of numbers using if statements
x, y =4, 5
if x<y:
    print(x)
else:
    print(y)

A = x if x<y else y
print(A)

c=10
if a>b and b>c:
     print("True")
else:
     print("False")

if a>b or b<c:
    print("True")
else:
    print("False")

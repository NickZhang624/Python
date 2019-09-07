# operator
print("C:\now")

print("C:\\now")

str = "C:\now"
print(str)

str = r"C:\now"
print(str)
print("-----------------------------")

# numbers
print(78 // 5)

print(3 ** 3)

print(78 / 5)
print("-----------------------------")


# string
print("I love {0}".format("Python"))
print("I love {a}".format(a="Python"))

string = "I love Python"
print(string[2:])

print(string[:1] + " realy " + string[2:])

print(string.center(50))

print(string.count("o"))

print(string.find("love"))

print(string.join("1234"))

print((string.center(50)).strip())

print(len(string))

print(string.replace("I", "You"))

#?????
print(string.partition(" "))
print((string.partition(" ")))

print(string.split(" "))

print("-----------------------------")

name = "nickzhang"
for i in name:
    print(i, end=",")

member = ["nick", "zhang", "athar", "ucol"]
for i in member:
    print(i, len(i))

print(range(5))
print(list(range(5)))

for i in range(5):
    print(i)

for i in range(2, 8):
    print(i)
for i in range(0, 10, 2):
    print(i)

number = "8"
answer = input("please enter a number?")

while True:
    if number == answer:
        break
    answer = input("Please try again!")
print("you are right")

for i in range(10):
    if i % 2 != 0:
        print(i)
        continue
    i += 2
    print(i)

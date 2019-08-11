# python

print("C:\now")

print("C:\\now")

str = "C:\now"
print(str)

str = r"C:\now"
print(str)

print(78 // 5)

print(3 ** 3)

print(78 / 5)

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

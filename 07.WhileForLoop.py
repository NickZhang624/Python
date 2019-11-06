#This is seventh part to introduce Python While loop

#The break Statement, The continue Statement
a = 2
while a < 6:
    print(a)
    a += 1
print("------------------")
while a < 10:
    print(a)
    if a == 6:
        break
    a += 1
print("--------------------")
while a <10:
    a += 1
    if a == 10:
        continue
    print(a)
print("=====================")


#for loop, for loop with list, for loop with range function
b = "nick"
for i in b:
    print(i)
print("=====================")
list =["nick", "zhang", "ucol"]
for i in list:
    print(i, len(i))
print("=====================")
for i in range(5):
    print(i)
print("=====================")
for i in range(0,10,2):
    print(i)

print("=====================")
for i in range(10):
    if i%2 == 0:
        print(i)
        continue
    i += 2
    print(i)

print("=====================")

ab =[1,2,3]
bc =["nick", "zhang", "ucol"]

for i in ab:
    for g in bc:
        print(i, g)

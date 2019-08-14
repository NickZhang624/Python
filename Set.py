# set------------------
num = {}
print(type(num))

num = {1,2,3,4,5}
print(type(num))

# set will clear duplicate data
num1 = {1,2,3,4,5,4,3,2,4,2}
print(num1)

# Can not index
# print(num1[1])

# clear duplicate data---- List
set1=[1,2,3,4,5,3,3,2,1]

temp =[]

for each in set1:
    if each not in temp:
        temp.append(each)

print(temp)

# use set to clear duplicate data
# from list to set then convert to list
print(list(set(set1)))


set2= {1,2,3}
set2.add(6)
print(set2)

set2.remove(2)
print(set2)

set3= frozenset([1,2,3,4,5])
print(type(set3))

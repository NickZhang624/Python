#This is fifth part to introduce Python Set
#Set is a collection which is unordered and unindexed. No duplicate members.

#List is a collection which is ordered and changeable. Allows duplicate members.(extension)
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.(extension)
#Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.(extension)

#A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
num = {}
print(type(num))

num = {1,2,3,4,5}
print(type(num))

# Set will clear duplicate data
num1 = {1,2,3,4,5,4,3,2,4,2}
print(num1)

# Can not index
print(num1[1])

# clear duplicate data---- List function
set1=[1,2,3,4,5,3,3,2,1]

temp =[]

for each in set1:
    if each not in temp:
        temp.append(each)

print(temp)

# use set to clear duplicate data
# from list to set then convert to list
print(list(set(set1)))

#add, remove function
set2= {1,2,3}
set2.add(6)
print(set2)

set2.remove(2)
print(set2)

set3= frozenset([1,2,3,4,5])
print(type(set3))

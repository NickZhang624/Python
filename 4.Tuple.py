#This is fourth part to introduce Python Tuple funtion
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

#List is a collection which is ordered and changeable. Allows duplicate members.(extension)
#Set is a collection which is unordered and unindexed. No duplicate members.(extension)
#Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.(extension)

#A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
tuple=("nick", "zhang", "ucol")
print(tuple)

#range of index
print(tuple[1])

print(tuple[:2])

print(tuple[1:])

# Add new element to tuple
temp=(tuple[:2]) + ("Athar", ) + (tuple[1:])
print(temp)

NewTuple = tuple[:]
print(NewTuple)

#query tuple type
tuple1=(1)
print(type(tuple1))

tuple2=(1,)
print(type(tuple2))

print(8*(8))
print(8*(8,))


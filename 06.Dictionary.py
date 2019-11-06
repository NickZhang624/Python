# This is sixth part to introduce Python Dictionary
#Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

#List is a collection which is ordered and changeable. Allows duplicate members.(extension)
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.(extension)
#Set is a collection which is unordered and unindexed. No duplicate members.(extension)

# Dic ={key: value}
#A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
dic = {1: "Nick", 2: "Zhang", 3:"Ucol"}
print(dic)

# index
print(dic[3])

# print value
print(list(dic.values()))

# change value
dic[3]="Athar"
print(dic)

# add new
dic[4]="ucol"
print(dic)

# fromkeys
dic2 = {}
print(dic2.fromkeys((1, 2, 3)))
print(dic2.fromkeys((1,2,3), "nothing"))
print(dic2.fromkeys((1,2,3), ("nick","zhang")))

# items
dic3={}
dic4 = dic3.fromkeys((range(4)),"Nick")
print(dic4)
for each in dic4.values():
    print(each)
for each in dic4.items():
    print(each)


# get
print(dic4.get(3))
print(dic4.get(4))

# clear
print(dic4.clear())
print(dic4)

# update

dic5 = {10: "nick"}
dic4.update(dic5)
print(dic4)

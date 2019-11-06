
# This is third part to introduce Python list function
# List is a collection which is ordered and changeable. Allows duplicate members.

# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.(extension)
# Set is a collection which is unordered and unindexed. No duplicate members.(extension)
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.(extension)

# A list is a collection which is ordered and changeable. In Python lists are written with square brackets.
# append, extend, insert functions
member = ["nick", "zhang"]
print(member)

member.append("Athar")
print(member)

member.append(["1", "2"])
print(member)

member.extend(["1", "2"])
print(member)

member.insert(0, "ucol")
print(member)

# remove, del, pop funtion
member = ["nick", "zhang", "athar", "ucol"]
member.remove("athar")
print(member)

del member[2]
print(member)

print(member.pop(0))


# slice funtion
member = ["nick", "zhang", "athar", "ucol"]
print(member[1:3])
print(member)

name = member[1:3]
print(name)

member2 = member[0:4]
print(member2)


# count, index, reverse, sort funtion
member = ["nick", "zhang", "athar", "ucol"]

print(member.count("nick"))

print(member.index("ucol"))

print(member.reverse())
print(member)

print(member.sort())
print(member)
print(member.reverse())
print(member)


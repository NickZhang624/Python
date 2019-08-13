
# List----------------------------------

# append, extend, insert
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

# remove, del, pop
member = ["nick", "zhang", "athar", "ucol"]
member.remove("athar")
print(member)

del member[2]
print(member)

print(member.pop(0))


# slice
member = ["nick", "zhang", "athar", "ucol"]
print(member[1:3])
print(member)

name = member[1:3]
print(name)

member2 = member[0:4]
print(member2)


# count, index, reverse, sort
member = ["nick", "zhang", "athar", "ucol"]

print(member.count("nick"))

print(member.index("ucol"))

print(member.reverse())
print(member)

print(member.sort())
print(member)
print(member.reverse())
print(member)


f = open('/Users/nick/Desktop/Movie.txt')
# print(f.read())
# print(f.read(10))


# print(f.seek(45, 0))
# print(f.readline())

# print(list(f))

# line = list(f)
# for each_line in line:
#    print(each_line)

# create new file and modify file
w = open('/Users/nick/Desktop/New.txt', 'w')
w.write("I love Python")
w.close()

z = open('/Users/nick/Desktop/New.txt')
print(z.read())






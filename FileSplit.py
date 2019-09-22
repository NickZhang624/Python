# This is task to split above movie dialogue
# No.1 Save dialogue to txt.file separately according to different people
# No.2 Save two dialogues to txt.file which split by "========"

f = open('/Users/nick/Desktop/Movie.txt')

jesse = []
celine = []
mark = []
chairwoman = []
movie1 = []
all = []
count = 0

# for each in f:
#     if each[:5] != "=====":
#         (people, dialogue) = each.split(":", 1)
#         if people == "Jesse":
#             jesse.append(people + ":" + dialogue)
#             j = open('/Users/nick/Desktop/Jesse.txt', "w")
#             j.writelines(jesse)
#         if people == "Celine":
#             celine.append(people + ":" + dialogue)
#             c = open('/Users/nick/Desktop/Celine.txt', "w")
#             c.writelines(celine)
#         if people == "Chairwoman":
#             chairwoman.append(people + ":" + dialogue)
#             h = open('/Users/nick/Desktop/Chairwoman.txt', "w")
#             h.writelines(chairwoman)
#         if people == "Mark":
#             mark.append(people + ":" + dialogue)
#             h = open('/Users/nick/Desktop/Mark.txt', "w")
#             h.writelines(mark)
#     else:
#         pass
# f.close()

# f = open('/Users/nick/Desktop/Movie.txt')
for eachmovie in f:
    w = eachmovie.split("\n")
    w.pop()
    all.append(w)
    count += 1
    # w = "list" + str(count)
    # count += 1
    print(all)


    # if w[:] != "======":
    #     print(w)
    # else:
    #     print(w)




        # (people, dialogue) = eachmovie.split(":", 1)
        # movie1.append(people + ":" + dialogue)
    # else:
    #     f.close()

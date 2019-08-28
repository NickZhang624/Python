# Jesse: In the months leading up to my wedding, I was thinking about you all the time. I mean, even on my way there; I’m in the car, a buddy of mine is driving me downtown and I’m staring out the window, and I think I see you, not far from the church, right? Folding up an umbrella and walking into a deli on the corner of 13th and Broadway. And I thought I was going crazy, but now I think it probably was you.
# Celine: I lived on 11th and Broadway.
# Jesse: You see?
# ============================================
# Mark Zuckerberg: As for any charges stemming from the breach of security, I believe I deserve some recognition from this board.
# Chairwoman: I’m sorry?
# Mark Zuckerberg: Yes?
# Chairwoman: I don’t understand.
# Mark Zuckerberg: Which part?


# This is task to split above movie dialogue
# No.1 Save dialogue to txt.file separately according to different people
# No.2 Save two dialogues to txt.file which split by "========"
f = open('/Users/nick/Desktop/Movie.txt')

jesse = []
celine = []
mark = []
chairwoman = []
movie1 = []

for each in f:
    if each[:5] != "=====":
        (people, dialogue) = each.split(":", 1)
        if people == "Jesse":
            jesse.append(people + ":" + dialogue)
            j = open('/Users/nick/Desktop/Jesse.txt', "w")
            j.writelines(jesse)
        if people == "Celine":
            celine.append(people + ":" + dialogue)
            c = open('/Users/nick/Desktop/Celine.txt', "w")
            c.writelines(celine)
        if people == "Chairwoman":
            chairwoman.append(people + ":" + dialogue)
            h = open('/Users/nick/Desktop/Chairwoman.txt', "w")
            h.writelines(chairwoman)
        if people == "Mark":
            mark.append(people + ":" + dialogue)
            h = open('/Users/nick/Desktop/Mark.txt', "w")
            h.writelines(mark)
    else:
        pass
f.close()


f = open('/Users/nick/Desktop/Movie.txt')
for eachmovie in f:
    if eachmovie[:5] != "======":
        (people, dialogue) = eachmovie.split(":", 1)
        movie1.append(people + ":" + dialogue)
    else:
        f.close()




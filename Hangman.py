import random

from pip._vendor.distlib.compat import raw_input


def chooseWord():
    file = open('/Users/nick/Desktop/words.txt')
    words = file.readlines()
    myword = 'a'
    while len(myword) < 4:
        myword = random.choice(words)
    myword = str(myword).strip('[]')
    myword = str(myword).strip("''")
    myword = str(myword).strip("\n")
    myword = str(myword).strip("\r")
    myword = myword.lower()
    return myword


def hangman():
    guesses = 0
    word = chooseWord()
    word_list = list(word)
    blanks = "_" * len(word)
    blanks_list = list(blanks)
    new_blanks_list = list(blanks)
    guess_list = []

    print("Let's play hangman!\nBut you only have 8 times allow you enter wrong letter!\n")
    print("Guess a letter.\n")

    while guesses < 8:
        guess = (str(raw_input("> "))).lower()

        if len(guess) > 1:
            print("Enter one letter at each time.")
        elif guess == "":
            print("Please enter a letter to play")
        elif guess in guess_list:
            print("You already guessed that letter! Here is what you've guessed:")
            print(' '.join(guess_list))
        else:
            guess_list.append(guess)
            i = 0
            while i < len(word):
                if guess == word[i]:
                    new_blanks_list[i] = word_list[i]
                i = i + 1

            if new_blanks_list == blanks_list:
                print("Your letter isn't here.")
                guesses = guesses + 1

                if guesses < 8:
                    print("Guess again.")
                    print(' '.join(blanks_list))

            elif word_list != blanks_list:

                blanks_list = new_blanks_list[:]
                print(' '.join(blanks_list))

                if word_list == blanks_list:
                    print("\nYOU WIN!")
                    print("Would you like to play again?")
                    print("Type 1 for yes or 2 for no.")
                    again = str(raw_input("> "))
                    if again == "1":
                        hangman()
                    quit()

                else:
                    print("Great guess! Guess another!")
    print("\nWhoops, you have already used 8 times to guess")
    print("Hangman programme will exit automatically\nSee you next time ")


hangman()











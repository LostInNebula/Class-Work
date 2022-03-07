def durdle_match(guess, target):
    '''
    Purpose: To function as a game in which user will input a five letter target word,
             and their guess as to what the target word is, with each guess
             returning five letters corresponding to if the letters in the guessed
             word are the correct letter, in the correct place of the target,
             the correct letter, in the wrong place of the target, or not a letter
             used in the target.
    Parameter: guess: the user's guess at what the target word may be
               target: the target word, chosen by user, to be guessed by user
    Return Value: feedback: five letters consisting of a combination of G, Y, and B,
                  representing if a letter in the guess is the correct letter in the correct
                  place in the correct place of the target, the correct letter, in the
                  wrong place of the target, or not a letter used in the target, respectively
    '''
    feedback = ""
    for i in range(5):
        if guess[i] == target[i]:
            feedback += "G"
        elif guess[i] in target:
            feedback += "Y"
        else:
            feedback += "B"
    return feedback


def durdle_game(target):
    '''
    Purpose: to function as a game in which user will input a five letter target word,
             and be given back five letters consisting of a combination of G, Y, and B,
             representing if a letter in the guess is the correct letter in the correct
             place in the correct place of the target, the correct letter, in the
             wrong place of the target, or not a letter used in the target, respectively
    Parameter: target: the target word that is to be guessed by the user
    Return Value: c: the amount of guesses the user has input
    '''
    print("Welcome to Durdle!")
    print("Enter a guess:")
    guess = input()
    c = 0
    for i in range(5):
        durdle_match(guess, target)
        feedback = durdle_match(guess, target)
        if feedback == "GGGGG":
            if c == 0:
                print(feedback)
                print("Congratulations, you got it in 1 guess!")
                return c + 1
            else:
                c += 1
                print(feedback)
                print(f"Congratulations, you got it in {c} guesses!")
                return c
        else:
            c += 1
            print(feedback)
            print("Enter a guess:")
            guess = input()

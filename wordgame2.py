from fileinput import filename
import random


def durdle_match(guess, target):
    '''
    Purpose:
        Determines which letters in the user's guess match the target
    Parameters:
        guess - a 5-letter string representing the user's guess
        target - a 5-letter string representing the target word
    Return Value:
        A 5-letter string, where each letter represents whether or not
        the letter in that position is correct.  'B' means the letter
        is not present in the target, 'Y' means that it's present in
        a different location, 'G' means it's in the correct location.
    '''
    matches = ''
    for i in range(5):
        if guess[i] not in target:
            matches += 'B'
        elif guess[i] == target[i]:
            matches += 'G'
        else:
            matches += 'Y'
    return matches

def durdle_game():
    '''
    Purpose:
        Lets the user play a game where they try to match a target word
    Parameters:
        None
    Return Value:
        The number of guesses it took the user to get the correct word.
    '''
    print("Welcome to Durdle!")
    guess = ''
    count = 0
    target = random.choice(get_word_list("words_full.txt"))
    while guess != target:
        guess = input("Enter a guess: ")
        if guess not in (get_word_list("words_full.txt")):
            print("Invalid guess, try again.")
        else:
            print('              '+durdle_match(guess, target))
            count += 1
    print("Congratulations, you got it in",count,"guesses!")
    return count

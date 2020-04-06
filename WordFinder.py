# File Name: Word Finder.py
# Purpose: Program that finds the position of a word in a phrase
# Date: 2015-01-05
# Last modified: 2020-03-01
# Author: Josen Pottackal
# Copy right no copyright
# Version: 1.0


# Finds the position of a word in a phrase.
# @param string User's phrase.
# @param word User's word.
def find_position(string, character):
    for j in range(len(string)):
        if str(string[j]) == str(character):
            positions.append(j + 1)


while True:
    positions = []
    print("This program will determine the positions a word appears in a phrase\n")

    phrase = input("Enter phrase:\n")
    editPhrase = (phrase.lower().split())  # Splits phrase into a list of separate lowercase words.

    word = input("Enter word:\n")
    editWord = word.lower()  # Converts word into lowercase.

    find_position(editPhrase, editWord)

    if len(positions) == 0:  # if the word not found then error message printed.
        print("The word was not found within the phrase, please try again:\n")
        continue
    else:
        print("The word appears in the position/s:", positions, "\n")  # if word is found the positions are printed.

    while True:
        answer = input("Would you like to restart the program?(yes/no):\n").lower()
        if answer in ("yes", "no"):  # if answer does not equal "yes" or "no", the program prints an error message.
            break
        print("Sorry I didn’t understand, please try again:\n")
    if answer == "yes":  # if answer equals "yes" the program restarts.
        continue
    else:
        print("End program\n")  # if answer equals "no" the program ends.
        break

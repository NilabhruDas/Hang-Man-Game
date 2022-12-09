import random
import os

name = input("Enter your Name : ")
print("Welcome", name.upper())
print("----------------------------------------------")
print("Try to guess the word in less than 10 attempts")


def getsingleword():
    with open("words.txt", 'r') as word:
        wordlist = word.readlines()
        impureword = wordlist[random.randint(0, len(wordlist)-1)]
        pureword = impureword.split('\n')
        return pureword[0]


def wordspace(l):
    for i in range(len(l)):
        print(l[i], end=" ")
    print()


def hangman(tries):
    print()
    arr = [
        ["-------------","\n"],
        ["      -  |","\n"],
        ["  ", " ", "o"],
        ["\n", " ", "--"], ["|"], ["--", "\n"],
        [" ", "  ", "|"],
        ["\n", " ", " ", "/"], ["\\"],
        [" "]
    ]
    for i in range(tries):
        for j in range(len(arr[i])):
            print(arr[i][j], end=" ")


word = getsingleword()
tries = 0
chance = 10
letters = set()
l = ["_" for i in range(len(word))]
wordspace(l)
hangman(tries)

while tries != chance:
    if word.upper() == ''.join(l):
        print("\nwooohh! I am going to live!")
        break
    guess = input("\n what could be the letter? :")
    os.system("cls")
    letters.add(guess)
    if len(letters) > 0:
        for i in letters:
            print("(", end=" ")
            print(i, end=" ")
            print(")", end=" ")
    print("\n")
    if guess in word:
        index = [i for i, l in enumerate(word) if l == guess]
        for i in index:
            l[i] = guess.upper()
    hangman(tries)
    print(" ")
    print(" ")
    wordspace(l)
    if guess not in word:
        tries += 1
        hangman(tries)
        print(" ")
        wordspace(l)
        print(" ")
        print(tries,"mistake")
else:
    print("\n I trust you")
    print(f"The word was {word}")

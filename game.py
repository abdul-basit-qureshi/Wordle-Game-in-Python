'''
*   The program presents a menu to the user/player to start the game. The
*   game-play requires the player to guess a 5-letter word in 6 tries. A try is valid if
*   the user enters a 5 letter word that is present in the dictionary. After the user has
*   entered a valid word, it needs to be compared against the solution. All the letters
*   that are in their correct place (compared to solution) are replaced by a '*' and all
*   the letters that are present in the solution but are out of place are replaced by a
*   '?'. A letter that is not present in the solution is replaced with a hyphen '-'.
*
*   Example word = Zonal (solution) not Case Sensitive
*   User Try 1:     break
*   program output: ---*-
*   User Try 2:     rolax
*   program output: -*?*-
*   User Try 3:     sonar
*   program output: -***-
*   User Try 4:     zonal
*   program output: *****   Correct! You Win!!
'''

from ast import main
from calendar import firstweekday
from fileinput import filename
from io import SEEK_SET
from msilib.schema import File
from types import NoneType
import numpy as np
import random
import glob

# global fptdict
# global fptsol

def printMenuChoice():
    print("****************************************************************")
    print("Welcome to text based Wordle game.\n")
    print("Enter your choice:\n")
    print("1. New game.")
    print("2. Instructions.")
    print("3. Exit.")
    choice = int(input())
    return choice

def printInstructions():
    print("*************************************************************************")
    print(" The Wordle game-play requires the player to guess a Five-letter word in")
    print(" six tries. A try is valid if the user enters a 5 letter word that is")
    print(" present in the dictionary. All the letters that are in their")
    print(" correct place (compared to solution) are replaced by a '*' and all the")
    print(" letters that are present in the solution but are out of place are replaced by")
    print(" a '?'. A letter that is absent in the solution is replaced with a hyphen '-'.\n")
    print(" Example word = Zonal (solution) not Case Sensitive.")
    print(" User Try 1:     break")
    print(" program output: ---*-")
    print(" User Try 2:     rolax")
    print(" program output: -*?*-")
    print(" User Try 3:     sonar")
    print(" program output: -***-")
    print(" User Try 4:     zonal")
    print(" program output: *****   Correct! You Win!!")


def gameplay(fptdict, fptsol):
    # print("Type of fptsol: ",type(fptsol))
    solutionWord = None
    playerGuess = None
    # Get a randon index into the solution file
    solIdx = random.randint(0,2314)
    solutionWord = readWordFromFile(solIdx, solutionWord, fptsol)
    print(f"The word at index {solIdx} is: {solutionWord}")

    attempt = 0
    while(attempt != 6):
        playerGuess = input(f"Try: {attempt} ")
        # Checks length if the enter word is of 5 letter
        if(len(playerGuess)==5):
            for i in range(12947):
                readWordFromFile(i, playerGuess, fptdict)
    quit()


def readWordFromFile(index, resWord,fpt):
    offset = index*7    
    # index*77 because 5 characters in word and one enter which takes 2 characters
    fpt.seek(offset)
    resWord = fpt.readline()
    return resWord
    

fptdict = open("data//dictionary.txt")
fptsol = open("data//solutions.txt")
userchoice = 2
while(userchoice != 3):
    userchoice = printMenuChoice()
    if(userchoice == 1):
        gameplay(fptdict, fptsol)
    elif(userchoice == 2):
        printInstructions()
    elif(userchoice == 3):
        print("Exiting the game!\n")
        quit()
    else:
        print("Enter a valid choice\n")

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

import random

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
    solutionWord = None
    playerWord = None
    # Get a randon index from 0 to 2314 into the solution file
    solIdx = random.randint(0,2314)
    solutionWord = readWordFromFile(solIdx, fptsol)
    # print(f"The word at index {solIdx} is: {solutionWord}")

    attempt = 0
    gameResult = [""]*5
    while(attempt != 6):
        foundInDict = 0
        playerWord = input(f"Try {attempt+1}:\t")
        playerWord = playerWord.lower()
        # Checks length if the user enter word is of 5 letter
        if(len(playerWord) == 5):
            for index in range(12947):
                # checking validity of word from dictionary
                checkWord = readWordFromFile(index, fptdict)
                if(checkWord == playerWord):
                    foundInDict = 1
                    break

            if(foundInDict):
                # considering one attempt when word found in dictionary and its length is 5
                attempt += 1

                # initializing other than *,-,? to every letter for every word
                for i in range(5):
                    gameResult[i] = '!'

                firstQuestionMarkIndex = []
                for i in range(5):
                    duplicatePastIndex = []
                    duplicatePresentIndex = []
                    duplicateLetter = None
                    duplicate = 0

                    for k in range(i-1,-1,-1):
                        # if playerWord has 2 same letters
                        if(playerWord[i] == playerWord[k]):
                            duplicate = 1
                            duplicatePastIndex.append(k)    # storing index of duplictate letters before this letter
                            duplicatePresentIndex.append(i)    # storing index of duplictate letters at present
                            duplicateLetter = playerWord[k]

                    # if any letter has a duplicate letter in playerWord
                    if(duplicate == 1):
                        for x in range(len(duplicatePresentIndex)):
                            # if present duplicate letter has already ?
                            if(gameResult[duplicatePresentIndex[x]] == '?'):
                                gameResult[duplicatePresentIndex[x]] = '-'

                        for x in range(len(duplicatePastIndex)):
                            # if past duplicate letter has already ?
                            if(gameResult[duplicatePastIndex[x]] == '?'):
                                gameResult[duplicatePastIndex[x]] = '-'

                        z = 0
                        for y in range(5):
                            # puts ? if duplicate letter in playerWord is also duplicate in solutionWord 
                            if((solutionWord[y] == duplicateLetter) and (playerWord[y] != solutionWord[y])):
                                # so it don't put ? on letter of solutionWord which is duplicate in playerWord 
                                if(len(duplicatePresentIndex) > z): # so that it doesn't show the error of list out of range
                                    if(duplicatePresentIndex[z] == i):
                                        z += 1
                                        continue
                                gameResult[i] = '?'

                    for j in range(5):
                        # puts ? if playerWord found in solutionWord in wrong position and there is no duplicate letter
                        if((playerWord[i] == solutionWord[j]) and (playerWord[j] != solutionWord[j]) and duplicate == 0):
                            gameResult[i] = '?'
                            firstQuestionMarkIndex.append(i)    # stores the index of first ? 

                    # puts * if playerWord found in same position as in solutionWord
                    if(playerWord[i] == solutionWord[i]):
                        gameResult[i] = '*'

                    # if letter doesn't found in solution word
                    if(gameResult[i] != '*' and gameResult[i] != '?'):
                        gameResult[i] = '-'

                for i in range(len(firstQuestionMarkIndex)):
                # puts ? to the first duplicate letter if * is not there
                    if(gameResult[firstQuestionMarkIndex[i]] != '*'):
                        gameResult[firstQuestionMarkIndex[i]] = '?'

                print("\t",*gameResult,sep="")

        # if playerGuess word mathces solutionWord
        if(playerWord == solutionWord):
            print("Congratulations! You Won")
            break
        # if attempts are over
        if(attempt == 6):
                print("You Lost the game!")
                print(f"Correct word was: {solutionWord}")
                break
        # if length is not 5 or word doesn't found in dictionary
        if(len(playerWord) != 5 or foundInDict == 0):
            print("Try again")


def readWordFromFile(index, fpt):
    # index*7 because 5 characters in word and one enter which takes 2 characters
    offset = index*7    
    fpt.seek(offset)
    # 5 because it reads only 5 letter word from that line leaving Enter
    resWord = fpt.readline(5)
    return resWord
    

if __name__ == "__main__":
    fptdict = open("data//dictionary.txt")
    fptsol = open("data//solutions.txt")
    userchoice = None
    while(userchoice != 3):
        userchoice = printMenuChoice()
        if(userchoice == 1):
            gameplay(fptdict, fptsol)
        elif(userchoice == 2):
           printInstructions()
        elif(userchoice == 3):
            print("\nExiting the game!\n")
            quit()
        else:
            print("Enter a valid choice\n")
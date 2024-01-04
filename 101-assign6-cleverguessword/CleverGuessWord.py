"""
Created on 11/22/23

@author: kennedyachugamonu
"""


import os
import random


def handleUserInputDifficulty():
    '''
    This function asks the user if they would like
    to play the game in (h)ard or (e)asy mode,
    then returns the corresponding number of misses
    allowed for the game.
    '''
    misses = 0
    print("How many misses do you want? Hard has 8 and Easy has 12.")
    choice = input("(h)ard or (e)asy> ")
    if choice == "h":
        misses = 8
    if choice == "e":
        misses = 12
        print("You have", misses, "to guess word")
    return misses




def createDisplayString(lettersGuessed, missesLeft, guessedWordAsList):
    '''
    Creates the string that will be displayed to the user, using the information
    in the parameters.
    '''
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in lettersGuessed:
        alphabet = alphabet.replace(letter, " ")
    display = ("letters not yet guessed: " + alphabet +
               "\nmisses remaining = " + str(missesLeft) + "\n" + " ".join(
                guessedWordAsList))
    return display


def handleUserInputLetterGuess(lettersGuessed, displayString):
    '''
    Prints displayString, then asks the user to input a letter to guess.
    This function handles the user input of the new letter guessed and checks if
    it is a repeated letter.
    '''
    print(displayString)
    guess = input("letter> ")
    while guess in lettersGuessed:
        print("you already guessed that")
        guess = input("letter> ")
    return guess

def handleUserInputDebugMode():
    '''
    This function decides if the user will play in debug or play mode. If the
    user inputs "d", True will be return. If the user inputs "p", False will be
    returned.
    '''
    answer = input("Which mode do you want: (d)ebug or (p)lay: ")
    if answer == "d":
        return True
    elif answer == "p":
        return False

def handleUserInputWordLength():
    '''
    This function will determine the length of the guessed word based on the
    integer the user inputs. The word length is assigned to the variable
    wordLength.
    '''
    wordLength = int(input("How many letters in the word you'll guess: "))
    return wordLength

def createTemplate(currTemplate, letterGuess, word):
    '''
    This function will change the template based on the letter the user guesses.
    It will return a string of the updated template.
    '''
    currTemplateList = list(currTemplate)
    for i in range(len(word)):
        if word[i] == letterGuess:
            currTemplateList[i] = letterGuess
    return "".join(currTemplateList)

def getNewWordList(currTemplate, letterGuess, wordList, debug):
    '''
    This function makes a dictionary of strings by calling createTemplate to
    add a key to the dictionary. wordList is then added to the list that maps to
    that key.
    '''
    gameDict = {}
    for word in wordList:
        check = createTemplate(currTemplate, letterGuess, word)
        if check not in gameDict:
            gameDict[check] = []
        gameDict[check].append(word)
    if debug == True:
        for k,v in sorted(gameDict.items()):
            print(k + " : " + str(len(v)))
        print("# keys =", len(gameDict.keys()))
    sortedKeys = sorted(gameDict.items(), key = lambda x: x[0].count("_"), reverse = True)
    maxWords = max(sortedKeys, key=lambda x: len(x[1]))
    for k, v in sortedKeys:
        if v == maxWords[1]:
            answer = (k, v)
            return answer
    return sortedKeys[0]

def processUserGuessClever(guessedLetter, guessedWordAsList, missesLeft):
    '''
    This function returns a list with the updated value of missesLeft as the
    first index and a boolean value of if the user made a correct guess or not.
    '''
    if guessedLetter not in guessedWordAsList:
        missesLeft -= 1
        return [missesLeft, False]
    else:
        return [missesLeft, True]
def runGame(filename):
    '''
    This function sets up the game, runs each round, and prints a final message
    on whether or not the user won. True is returned if the user won the game.
    If the user lost the game, False is returned.
    '''

    file = os.path.join(filename)
    wordfile = open(file)
    WordList = [w.strip() for w in wordfile]
    debug = handleUserInputDebugMode()
    wordLength = handleUserInputWordLength()
    missesLeft = handleUserInputDifficulty()
    wordList = []
    for word in WordList:
        if len(word) == wordLength:
            wordList.append(word)
    lettersGuessed = []
    guessesAmount = 0
    guessedWordAsList = []
    randomWord = random.choice(wordList)
    for c in randomWord:
        guessedWordAsList.append("_")
    TotalMissesCounter = missesLeft
    while "_" in guessedWordAsList and missesLeft >= 0:
        displayString = createDisplayString(lettersGuessed, missesLeft, guessedWordAsList)
        if debug:
            displayString += "\n" + "(word is " + randomWord + ")" + "\n" + "# possible words: " + str(len(wordList))
        letterGuess = handleUserInputLetterGuess(lettersGuessed, displayString)
        lettersGuessed.append(letterGuess)
        currTemplate = "".join(guessedWordAsList)
        newGetWord = getNewWordList(currTemplate, letterGuess, wordList, debug)
        guessedWordAsList = list(newGetWord[0])
        wordList = newGetWord[1]
        randomWord = random.choice(wordList)
        cleverGuess = processUserGuessClever(letterGuess, guessedWordAsList, missesLeft)
        missesLeft = cleverGuess[0]
        if not cleverGuess[1]:
            print("you missed: " + letterGuess + " not in word")
        guessesAmount += 1
    if guessedWordAsList == list(randomWord):
        print("you guessed the word: " + randomWord)
    else:
        print("you're hung!!" + "\n" + "word is " + randomWord)
    print("you made " + str(guessesAmount) + " guesses with " + str(
                TotalMissesCounter - missesLeft) + " misses")
    if guessedWordAsList == list(randomWord):
        return True
    else:
        return False



if __name__ == "__main__":
    '''
    Running GuessWord.py should start the game, which is done by calling runGame,
    therefore, we have provided you this code below.
    '''
    playGame = True
    record = [0, 0]
    while playGame == True:
        outcome = runGame("lowerwords.txt")
        if outcome == True:
            record[0] += 1
        else:
            record[1] += 1
        playAgain = input("Do you want to play again? y or n> ")
        if playAgain == "y":
            playGame = True
        else:
            playGame = False
            print("You won " + str(record[0]) + " game(s) and lost " + str(record[1]))


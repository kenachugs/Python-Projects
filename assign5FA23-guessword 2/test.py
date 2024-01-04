'''
Description:
        You must create a Guess the Word game that
        allows the user to play and guess a secret word.
        See the assignment description for details.

@author: kennedyachugamonu, kia2
'''

import random
import os.path


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


def getWord(words, length):
    '''
    Selects the secret word that the user must guess.
    This is done by randomly selecting a word from words that is of length
    length.
    '''
    LengthWordsList = []
    for word in words:
        if len(word) == length:
            LengthWordsList.append(word)
    randomIndex = random.randint(0, len(LengthWordsList) - 1)
    return LengthWordsList[randomIndex]


def createDisplayString(lettersGuessed, missesLeft, guessedWordAsList):
    '''
    Creates the string that will be displayed to the user, using the information
    in the parameters.
    '''
    display = ("letters you've guessed: " + " ".join(sorted(lettersGuessed)) +
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
    n = 0
    while n == 0:
        guess = input("letter> ")
        if guess in lettersGuessed:
            print("you already guessed that")
        else:
            n += 1
            return guess
    # while guess in lettersGuessed:
    # print("you've already guessed that")
    # guess = input("letter> ")


def updateGuessedWordAsList(guessedLetter, secretWord, guessedWordAsList):
    '''
    Updates guessedWordAsList according to whether guessedLetter is in
    secretWord and where in secretWord guessedLetter is in.
    '''

    for i in range(len(secretWord)):
        if secretWord[i] == guessedLetter:
            guessedWordAsList[i] = guessedLetter
    return guessedWordAsList


def processUserGuess(guessedLetter, secretWord, guessedWordAsList, missesLeft):
    '''
    Uses the information in the parameters to update the user's progress in
    the Guess the Word game.
    '''
    if guessedLetter in secretWord:
        guessedWordAsList = updateGuessedWordAsList(guessedLetter, secretWord,
                                                    guessedWordAsList)
        guessBool = True
    else:
        missesLeft -= 1
        guessBool = False
    currentInfo = [guessedWordAsList, missesLeft, guessBool]
    return currentInfo


def runGame(filename):
    '''
    This function sets up the game, runs each round, and prints a final message
    on whether or not the user won. True is returned if the user won the game.
    If the user lost the game, False is returned.
    '''
    file = os.path.join(filename)
    wordFile = open(file)
    WordsList = []
    for line in wordFile:
        WordsList.append(line.strip())
    # f.close()
    length = random.randint(5, 10)
    secretWord = getWord(WordsList, length)
    guessedWordAsList = []
    secretWordAsList = []
    for i in range(len(secretWord)):
        secretWordAsList.append(secretWord[i])
        guessedWordAsList.append("_")
    missesLeft = handleUserInputDifficulty()
    totalMissesCounter = missesLeft
    numOfGuesses = 0
    lettersGuessed = []
    while missesLeft >= 0 or guessedWordAsList != secretWordAsList:
        print(guessedWordAsList)
        print(secretWordAsList)
        displayString = createDisplayString(lettersGuessed, missesLeft,
                                            guessedWordAsList)
        guessedLetter = handleUserInputLetterGuess(lettersGuessed,
                                                   displayString)
        lettersGuessed.append(guessedLetter)
        numOfGuesses += 1
        userGuess = processUserGuess(guessedLetter, secretWord,
                                     guessedWordAsList, missesLeft)
        guessedWordAsList = userGuess[0]
        missesLeft = userGuess[1]
        if userGuess[2] == False:
            print("you missed: " + guessedLetter + " not in word")
        if guessedWordAsList == secretWordAsList:
            print("you guessed the word: " + secretWord)
            print("you made " + str(numOfGuesses) + " guesses with " + str(
                totalMissesCounter - missesLeft) + " misses")
            # return True
        if missesLeft == 0:
            print("you're hung!!")
            print("word is " + secretWord)
            print("you made " + str(numOfGuesses) + " guesses with " + str(
                totalMissesCounter - missesLeft) + " misses")
            # return False
        if guessedWordAsList == secretWordAsList:
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
            print("You won " + str(record[0]) + " game(s) and lost " + str(
                record[1]))





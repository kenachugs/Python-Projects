"""
Created on 10/23/23

@author: kennedyachugamonu
"""
shift = 3
lower_alph = "abcdefghijklmnopqrstuvwxyz"
upper_alph = lower_alph.upper()
shifted_lower = lower_alph[3:] + lower_alph[:3]
shifted_upper = upper_alph[3:] + upper_alph[:3]

def encrypt(w):
    '''
    encrypts w depending on the assigned shift by finding if it is a lowercase
    or uppercase letter or if its another character, then concatenates that
    to newW
    '''
    newW = ""

    for i in w:
        if i in lower_alph:
            index = lower_alph.index(i)
            newW += shifted_lower[index]
        elif i in upper_alph:
            index = upper_alph.index(i)
            newW += shifted_upper[index]
        else:
            newW += i
    return newW

def setShift(num):
    '''
    sets the shift necessary to get w encrypted to the proper Caesar shift
    depending on the inputted integer
    '''
    global shift, shifted_lower, shifted_upper
    shift = num
    shifted_lower = lower_alph[num:] + lower_alph[:num]
    shifted_upper = upper_alph[num:] + upper_alph[:num]

def findShift(words):
    '''
    to find the shift, this function goes through all 26 possible shifts for
    words to see which shift yields the most real words. findShift does this
    by comparing the sets of the wordsClean and compare to see what words they
    have in common.
    '''
    import os.path
    file = os.path.join("data", "lowerwords.txt")
    f = open(file)
    wordsClean = [w.strip() for w in f.read().split()]
    wordsClean = set(wordsClean)
    compare = []
    remainWords = 0
    remainWordsList = []
    for i in range(26):
        setShift(i)
        encrypted = encrypt(words)
        compare = encrypted.split(" ")
        compare = set(compare)
        remainWords = len(wordsClean & compare)
        remainWordsList.append(remainWords)
    bestSolutionIndex = max(remainWordsList)
    lengthOfBestSolution = remainWordsList.index(bestSolutionIndex)
    return 26 - lengthOfBestSolution

if __name__ == '__main__':
    setShift(3)
    print(encrypt("Hat 7"))
    print(findShift("Zkdw grhv wkh ira vdb?"))

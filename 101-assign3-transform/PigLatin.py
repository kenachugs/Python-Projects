"""
Created on 10/22/23

@author: kennedyachugamonu
"""

def encrypt(w):
    """
    checks the letters of w starting with the first letter to see if it is a
    vowel. If not, it follows the Pig Latin rules for words that start with
    consonants
    """
    encryptWord = ""

    #checks words that start with a vowel
    if w[0] in "aeiou" or w[0] in "AEIOU":
        encryptWord = w + "-way"
        return encryptWord

    #checks words that start with "qu" or "QU"
    elif w[0:2] == "qu" or w[0:2] == "QU":
        temp = w[0:2]
        encryptWord = w[2:]
        count = 0
        remain = ""
        for i in encryptWord:
            if i in "aeiou" or i in "AEIOU":
               break
            else:
                remain += i
                count += 1
        return encryptWord[count:] + "-" + temp + remain + "ay"

    #checks words that have start with a consonant but have a vowel later
    elif w[0] not in "aeiou" and w[0] not in "AEIOU":
        for i in range(1, len(w)):
            if w[i] in "aeiou" or w[i] in "AEIOU":
                encryptWord = w[i:] + "-" + w[0:i] + "ay"
                return encryptWord
            else:
                i += 1

    # checks words that don't have any vowels in them
    consonants = 0
    word = ""
    for i in range(len(w)):
        if (w[i] not in "aeiou" and w[i] not in "AEIOU"):
            if w.find("y") > 0:
                return w[w.find("y"):] + "-" + w[0:w.find("y")] + "ay"
            consonants += 1

    if consonants == len(w):
        return w + "-way"


def decrypt(w):
    '''
    splits w at the last hyphen and then creates the original word by adding
    all the letters before "ay" and the edited word together
    '''
    wList = w.rsplit("-")
    wIndex = wList[1].find("ay")
    orgWord = wList[1][:wIndex] + wList[0]
    return orgWord

if __name__ == '__main__':
    print(encrypt("'always!'"))

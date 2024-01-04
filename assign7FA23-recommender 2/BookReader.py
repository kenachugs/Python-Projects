'''
@kennedyachugamonu, kia2
'''


def getdata():
    '''
    This function reads data from a file and returns the data in the form of a two-tuple.
    The first element of the two-tuple is a list of strings, the second element is a 
    dictionary.
    '''
    f = open("books.txt", "r")
    lst = [l.strip().split(",") for l in f.readlines()]
    books = []
    ratings = {}
    for line in lst:
        idx = 0
        while idx < len(line):
            #index 0 contains the student's name
            if idx == 0:
                student = line[0]
                ratings[student] = []
            #odd indeces contain the books
            elif idx % 2 == 1:
                if line[idx] not in books:
                    books.append(line[idx])
            #even indeces contain the ratings
            else:
                student = line[0]
                ratings[student].append(int(line[idx]))
            idx += 1
    return (books, ratings)

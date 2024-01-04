'''
@kennedyachugamonu, kia2
'''

def getdata():
    '''
    This function reads data from a file and returns the data in the form of a two-tuple.
    The first element of the two-tuple is a list of strings, the second element is a 
    dictionary.
    '''
    f = open("movies.txt", "r")
    #each line is split into a list with each element being what was seperated by a comma
    lst = [l.strip().split(",") for l in f.readlines()]
    movieList = []
    studentList = []
    dict = {}
    for i in lst:
        student = i[0]
        studentList.append(student)
        movie = i[1]
        movieList.append(movie)
        rating = i[2]
        if student not in dict:
            dict[student] = []
    #sets is made so there are no repeats, then sorted converts them back to lists
    studentSet = sorted(set(studentList))
    movieSet = sorted(set(movieList))
    for student in studentSet:
        idx3 = 0
        while idx3 < len(movieSet):
            dict[student].append(0)
            idx3 += 1

    idx = 0
    while idx < len(movieSet):
        movieName = movieSet[idx]
        idx2 = 0
        while idx2 < len(lst):
            student = lst[idx2][0]
            movie = lst[idx2][1]
            ranking = lst[idx2][2]
            if movie == movieName:
                dict[student][idx] = int(ranking)
            idx2 += 1
        idx += 1
    f.close()
    return (movieSet, dict)



'''
@kennedyachugamonu, kia2
'''
import json
import os
def averages(items, ratings):
    '''
    This function calculates the average ratings for items. 
    A two-tuple is returned, where the first element is a string and the second element is a float.
    '''
    ListOfAllRatings = []
    i = 0
    for item in items:
        avg = 0
        users = 0
        for rating in ratings.values():
            if rating[i] != 0:
                avg += rating[i]
                users += 1
        #edge case for if there are no users
        if users == 0:
            avg = 0.0
        else:
            avg = avg/users
        ListOfAllRatings.append((item,avg))
        i += 1
    inOrder = sorted(ListOfAllRatings, key = lambda x: x[0])
    #sorts according to the avg value in the tuple from max to min
    return(sorted(inOrder, key=lambda x: x[1], reverse = True))


def similarities(name, ratings):
    '''
    This function calculates how similar the rater called name is to all other raters.
    A two-tuple is returned, where the first element is a string and the second element is an integer.
    '''
    lst = []
    for user, nums in ratings.items():
        if user != name:
            count = 0
            tempList = [0,0]
            lst1 = ratings[name]
            lst2 = ratings[user]
            for i in range(len(lst1)):
                tempList[0] = lst1[i]
                tempList[1] = lst2[i]
                #dot product is being performed here
                count += (tempList[0]*tempList[1])
            lst.append((user, int(count)))
    lst = sorted(lst, key = lambda x: (-x[1], x[0]))
    return lst
def recommendations(name, items, ratings, numUsers):
    '''
    This function calculates the weighted average ratings and makes recommendations 
    based on the parameters and weighted average. A two-tuple is returned, where 
    the first element is a string and the second element is a float.
    '''
    similarity = similarities(name, ratings)
    similarity = similarity[:numUsers]
    dict = {}
    lst = []
    for s in similarity:
        currentRater = s[0]
        if currentRater != name:
           for r in ratings[currentRater]:
               #multiplies each rating by the weight of the user
               newVal = r * s[1]
               lst.append(newVal)
        dict[currentRater] = lst
        lst = []
    average = averages(items, dict)
    return average




if __name__ == '__main__':
    items = ['Tiger', 'Dog', 'Snake', 'Fireball']
    ratings = {'Liam': [0, 0, 0, 0], 'Man-Lin': [0, 0, 0, 0],
               'Jose': [0, 0, 0, 0]}
    print(averages(items,ratings))
    print(similarities('Tiger', ratings))

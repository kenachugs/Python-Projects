'''
@kennedyachugamonu, kia2
'''
import RecommenderEngine

def makerecs(name, items, ratings, numUsers, top):
    '''
    This function calculates the top recommendations and returns a two-tuple consisting of two lists. 
    The first list is the top items rated by the rater called name (string).
    The second list is the top items not seen/rated by name (string)
    '''
    recommendations = RecommenderEngine.recommendations(name, items, ratings, numUsers)
    rankedList = []
    unrankedList = []
    nameRanking = ratings[name]
    for recommendation in recommendations:
        #gets the movie name by indexing in items
        idx = items.index(recommendation[0])
        #since the lists are parallel, we get the corresponding rating in nameRanking
        movieName = nameRanking[idx]
        #if movieName == 0, then it wasn't ranked
        if movieName != 0:
            rankedList.append(recommendation)
        else:
            unrankedList.append(recommendation)
    #rankedList is sorted in descending order
    rankedList = sorted(rankedList, key = lambda x: x[1], reverse = True)
    #slices ranked list to only have to top length tuples
    rankedList = rankedList[:top]
    #unrankedList is sorted in descending order
    unrankedList = sorted(unrankedList, key=lambda x: x[1], reverse=True)
    #slices unrankedList to only have top length tuples
    unrankedList = unrankedList[:top]

    return (rankedList, unrankedList)

if __name__ == '__main__':
    pass
             




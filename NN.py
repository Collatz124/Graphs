import numpy as np 

def nearestNeighbour (weightMatrix: np.array, startingIndex: int) -> []:
    """ Find en hamilton kreds ved hjælp af nærmeste nabo algoritmen """
    path = [startingIndex]

    n = np.shape(weightMatrix)[0] # Antallet af punkter

    # Loop ind til alle punkter er tilføjet
    while (len(path) < n):

        # Find den punktet tættest på det nuværende:
        nearest = None
        previusNode = path[-1] - 1 # Det sidst besøgte punkts index i matricen

        for i in range(n):
            if (((i + 1) in path) == False): # Kig kun på punkter der ikke allerede er i vejen.
                if (nearest == None): nearest = i # Hvis det er det første ikke besøgte punkt der kigges på.
                else:
                    if (weightMatrix[previusNode][i] < weightMatrix[previusNode][nearest]): nearest = i

        # Tilføj det tætteste punkt til vejen
        path.append(nearest + 1)


    return path + [startingIndex] # Gå tilbage til det første punkt

def computeDistance (route: [int]) -> int:
    """ Computes the total distance of the route """
    total = 0
    for i in range(len(route) - 1):
        total += W[route[i] - 1][route[i + 1] - 1] # Tager højde for at python index starter ved 0
    return total 

if (__name__ == "__main__"):
    # Vægt matrice 
    W = [[    np.inf,   15,   51,   70,   96,   58,   45,    7,   16,   37],
         [  15,     np.inf,   42,   66,   99,   59,   50,   19,   31,   47],
         [  51,   42,     np.inf,   28,   74,   39,   43,   49,   64,   88],
         [  70,   66,   28,     np.inf,   49,   26,   41,   66,   80,  107],
         [  96,   99,   74,   49,     np.inf,   40,   51,   90,   99,  126],
         [  58,   59,   39,   26,   40,     np.inf,   16,   52,   63,   91],
         [  45,   50,   43,   41,   51,   16,     np.inf,   38,   48,   75],
         [   7,   19,   49,   66,   90,   52,   38,     np.inf,   15,   40],
         [  16,   31,   64,   80,   99,   63,   48,   15,     np.inf,   27],
         [  37,   47,   88,  107,  126,   91,   75,   40,   27,     np.inf]]


    C = nearestNeighbour(np.array(W), 1)
    print("C: {0} D(C): {1}".format(C, computeDistance(C)))
    # OUTPUT: C: [1, 8, 9, 10, 2, 3, 4, 6, 7, 5, 1] D(C): 355
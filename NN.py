import numpy as np 
from misc.misc import computeDistance

def nearestNeighbour (W: [[float]], startingIndex: int) -> []:
    """ Find en hamilton kreds ved hjaelp af naermeste nabo algoritmen """
    path = [startingIndex]
    n = np.shape(W)[0] # Antallet af punkter
    notVisitedYet = list(range(1, n + 1))
    notVisitedYet.remove(startingIndex)
    
    # Loop ind til alle punkter er tilfoejet
    while (len(path) < n):
        # Find punktet taettest paa det nuvaerende:
        nearest = None
        previusNode = path[-1] - 1 # Det sidst besoegte punkts index i matricen
        bestDistance = np.inf # Saettes til uendeligt saa nearest saettes til i ved det foeste punkt
        
        for i in notVisitedYet:
            distance = W[previusNode][i - 1] # Tag hoejde for at python index starter ved 0
            if (distance < bestDistance): 
                nearest = i
                bestDistance = distance

        path.append(nearest) # Tilfoej det taetteste punkt til vejen 
        notVisitedYet.remove(nearest)
        
    return path + [startingIndex] # Gaa tilbage til det foerste punkt

if (__name__ == "__main__"):
    # Vaegt matrix 
    W = [[np.inf,15,51,71,97,58,46,7,16,37],
         [15,np.inf,42,66,100,60,57,20,31,48],
         [51,42,np.inf,29,74,39,44,49,64,88],
         [71,66,29,np.inf,49,27,41,66,80,107],
         [97,100,74,49,np.inf,40,51,90,99,126],
         [58,60,39,27,40,np.inf,17,52,63,91],
         [46,51,44,41,51,17,np.inf,39,48,76],
         [ 7,20,49,66,90,52,39,np.inf,15,41],
         [16,31,64,80,99,63,48,15,np.inf,28],
         [37,48,88,107,126,91,76,41,28,np.inf]]
    C = nearestNeighbour(W, 1)
    print("C: {0}, D(C): {1}".format(C, computeDistance(W, C)))
    # OUTPUT: C: [1, 8, 9, 10, 2, 3, 4, 6, 7, 5, 1], D(C): 355
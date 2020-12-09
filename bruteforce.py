from itertools import permutations
from misc import computeDistance

def bruteForce (W: [[float]], nodes: [int]) -> ([int]):
    """ Bruteforce løsning af den handelsrejsendes problem """
    # Genere samtlige mulige hamilton kredse 
    # Denne tjekker den samme hamilton kreds flere gange (baglaens og forlaens)
    curcuits = [list(P) + [P[0]] for P in permutations(nodes)]

    n = len(curcuits) # Antallet af kredse
    print("Posible Hamilton curcuits: {0}".format(n))

    # Tjek den foerste af hamilton kredsene
    bestCurcuit = curcuits[0]
    bestDistance = computeDistance(W, bestCurcuit) # Finder vejens vaegt.

    # Tjekker de resterende hamilton kredse igennem
    for index, c in enumerate(curcuits[1:]):
        distance = computeDistance(W, c)
        if distance <= bestDistance:
            bestCurcuit = c
            bestDistance = distance

    return bestCurcuit

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

    nodes = list(range(1, 11))
    C = bruteForce(W, nodes)
    print("C = {0}, D(C) = {1}".format(C, computeDistance(W, C)))
    # OUTPUT: C = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10], D(C) = 307
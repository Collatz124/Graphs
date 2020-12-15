from itertools import permutations
from misc.misc import computeDistance
import numpy as np

def bruteForce (W: [[float]], nodes: [int], start: int) -> ([int]):
    """ Bruteforce loesning af den handelsrejsendes problem """
    # Genere samtlige mulige hamilton kredse 
    # Denne tjekker den samme hamilton kreds flere gange (baglaens og forlaens)
    circuits = [list(P) + [P[0]] for P in permutations(nodes)]
    # Soerger for at der kun kigges paa de kredse med startpunkt i v_start
    circuits = list(filter(lambda x: x[0] == start, circuits))
    print("Posible Hamilton curcuits: {0} with start in v[{1}]".format(len(circuits), start)) 

    # Tjek den foerste af hamilton kredsene
    bestCircuit = circuits[0]
    bestDistance = computeDistance(W, bestCircuit) # Finder vejens vaegt.

    # Tjekker de resterende hamilton kredse igennem
    for index, c in enumerate(circuits[1:]):
        distance = computeDistance(W, c)
        if distance < bestDistance:
            bestCircuit = c
            bestDistance = distance

    return bestCircuit

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
    C = bruteForce(W, nodes, 1)
    print("C = {0}, D(C) = {1}".format(C, computeDistance(W, C)))
    # OUTPUT: C = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1], D(C) = 311
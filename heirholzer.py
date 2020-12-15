import numpy as  np

def findNeighboor (W: [[int]], node: int, n: int):
    """ Finds a neighbour to the node at the index given """
    for i in range(n):
        if (W[node][i] != np.inf):
            # Opdater vægt matricen
            W[node][i], W[i][node] = np.inf, np.inf
            return (W, i

def findSimpleCurcuit (W: [[float]], node: int):
    """ Find en simpel kreds med start i 'node' """
    # Dan den simple kreds C
    C = [node]
    W, k = findNeighboor(W, C[-1], len(W)) # Matricen er kvadratisk
    while k != node:
        C.append(k)
        W, k = findNeighboor(W, k, len(W))
        
    # Gør C til en kreds
    C.append(k)
    return W, C

def hasUsedAllEdges (W: [[float]]):
    """ Checks if """
    for i in range(len(W)):
        for j in range(i, len(W)):
            if (W[i][j] != np.inf): return False
    return True
        
def Heirholzer (W: [[float]]):
    W, P = findSimpleCurcuit(W, 0) # Dan den simple kreds P 
    # (NOTE: denne funktion fjerner også løbende kanterne fra vægt matricen)
    while (hasUsedAllEdges(W) == False): # Så længe der er kanter tilbage
        for index, v in enumerate(P):
            # Tjek om v er incident med nogle kanter i delgrafen H
            isVIncident = False
            for i in range(len(W)):
                if (W[v][i] != np.inf):
                    isVIncident = True
            
            # Dan kredsen Q, hvis v er incident med en kant i H
            if (isVIncident == True):
                # Dan den simple kreds Q 
                W, Q = findSimpleCurcuit(W, v)
                
                # Tilføj Q, men uden startpunktet U
                P = P[:index + 1] + Q[1:] + P[index + 1:]
                break # Hop ud nu hvor P er modificeret
    
    return P
            
                    
        
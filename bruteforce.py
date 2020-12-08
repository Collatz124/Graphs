from itertools import permutations
import numpy as np

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

nodes = list(range(1, 11))

# Generate routes
routes = [list(r) + [r[0]] for r in permutations(nodes)] # Danner hamilton kredsene

# En funktion som beregner vægten af en vej
def computeDistance (route: [int]) -> int:
    total = 0
    for i in range(len(route) - 1):
        total += W[route[i] - 1][route[i + 1] - 1] # Tager højde for at python index starter ved 0
    return total

# Check all routes
bestRoute = routes[0]
bestDistance = computeDistance(bestRoute)

n = len(routes)
print("Posible Hamilton curcuits: {0}".format(n))

# Tjekker alle de resterende hamilton kredse igennem
for index, r in enumerate(routes[1:]):
    distance = computeDistance(r)
    if distance <= bestDistance:
        bestRoute = r
        bestDistance = distance
    if (index % 100000 == 0):
        print("{0:.1f} %".format(index / n * 100))

print("C = {0}, D(C) = {1}".format(bestRoute, bestDistance))
# OUTPUT: C = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10], D(C) = 307
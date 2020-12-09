# En funktion som beregner vægten af en vej
def computeDistance (W: [[float]], route: [int]) -> int:
    total = 0
    for i in range(len(route) - 1):
        total += W[route[i] - 1][route[i + 1] - 1] # Tager højde for at python index starter ved 0
    return total
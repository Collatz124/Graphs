# Den her skal ikke afleveres

import numpy as np 

W = [[   0,   15,   51,   71,   97,   58,   46,    7,    16,   37],
     [  15,   0,    42,   66,   100,  60,   57,    20,   31,   48],
     [  51,   42,   0,    29,   74,   39,   44,    49,   64,   88],
     [  71,   66,   29,   0,    49,   27,   41,    66,   80,  107],
     [  97,   100,  74,   49,    0,   40,   51,    90,   99,  126],
     [  58,   60,   39,   27,   40,    0,   17,    52,   63,   91],
     [  46,   51,   44,   41,   51,   17,    0,    39,   48,   76],
     [   7,   20,   49,   66,   90,   52,   39,    0,    15,   41],
     [  16,   31,   64,   80,   99,   63,   48,   15,    0,    28],
     [  37,   48,   88,   107,  126,  91,   76,   41,   28,     0]]
     
n = int(input("Number of nodes: "))
r = float(input("Radius to center: "))

for i in range(n):
    string = ""
    for j in range(n):
        if (j != n - 1):
            string += (str(W[i][j]) if (W[i][j] != 0) else "*") + " & "
        else:
            string += (str(W[i][j]) if (W[i][j] != 0) else "*") + " \\\\"

    print(string)

# Print punkterne
for i in range(n):
    print(f"\\node[punkt] at ({round(np.cos(2 * np.pi / n * i) * r, 1)}, {round(np.sin(2 * np.pi / n * i) * r, 1)}) (v_{i + 1}) {{$v_{{{i + 1}}}$}};")

"""# Print Kanter
for i in range(n - 1):
    for j in range(i, n):
        if (i != j):
            print(f"\\draw [-, thick, draw=black] (v_{i + 1}) -- node[below]{{${W[i][j]}$}} (v_{j + 1});")"""
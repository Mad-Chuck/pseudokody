with open("pieczywo.txt") as f:
    pieczywo = f.read().splitlines()
    pieczywo = [i.split() for i in pieczywo]
    for i, row in enumerate(pieczywo):
        for j, elem in enumerate(row):
            pieczywo[i][j] = int(elem)

for i in range(len(pieczywo)):
    indeksy = [i for i in range(9)]
    for j in range(5):
        najmniejszy = j
        for k in range(j+1,9):
            if pieczywo[i][k] > pieczywo[i][najmniejszy]:
                najmniejszy = k
        pieczywo[i][j],pieczywo[i][najmniejszy] = pieczywo[i][najmniejszy],pieczywo[i][j]
        indeksy[j],indeksy[najmniejszy] = indeksy[najmniejszy], indeksy[j]
    print(indeksy[4])

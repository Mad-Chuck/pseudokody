with open("pomiary.txt") as f:
    pomiary = [line.split() for line in f.read().splitlines()]
    for i, row in enumerate(pomiary):
        pomiary[i] = [int(elem) for elem in row]

ileNieparzystych = 0
nieparzyste = [None]*5
iterator = 0

pomiary = [
    [912, 382, 283, 54, 3423, 804, 200, 177, 20, 373],
    [7123, 362, 23, 54, 33, 50, 390, 112, 155, 983],
    [1662, 32, 233, 54, 342, 980, 99, 43, 400, 508],
    [162, 3213, 223, 54, 343, 54, 68, 98, 317, 289],
    [132, 32, 213, 54, 423, 675, 66, 88, 557, 863]
]

for i in range(5):
    for j in range(10):
        if pomiary[i][j] % 2 != 0:
            ileNieparzystych = ileNieparzystych + 1
            if ileNieparzystych == 6:
                break
            nieparzyste[iterator] = pomiary[i][j]
            iterator = iterator + 1

    if ileNieparzystych == 5:
        liczba = 0
        indeks = 0

        for j in range(1, 5):
            liczba = nieparzyste[j]
            indeks = j

            while indeks > 0 and liczba > nieparzyste[indeks - 1]:
                nieparzyste[indeks] = nieparzyste[indeks - 1]
                indeks = indeks - 1

            nieparzyste[indeks] = liczba

        print(nieparzyste)

    ileNieparzystych = 0
    iterator = 0

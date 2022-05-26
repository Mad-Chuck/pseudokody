with open("pracownicy.txt") as f:
    pracownicy = f.read().splitlines()
    pracownicy = [i.split() for i in pracownicy]
    for i, row in enumerate(pracownicy):
        for j, elem in enumerate(row):
            pracownicy[i][j] = int(elem)

for i in range(0, 49 + 1):
    for j in range(0, 5 + 1):
        minimum = j
        maximum = j

        for k in range(j + 1, 29 - j + 1):

            if pracownicy[i][k] < pracownicy[i][minimum]:
                minimum = k
            if pracownicy[i][k] > pracownicy[i][maximum]:
                maximum = k

        pracownicy[i][j], pracownicy[i][minimum] = pracownicy[i][minimum], pracownicy[i][j]
        pracownicy[i][29 - j], pracownicy[i][maximum] = pracownicy[i][maximum], pracownicy[i][29 - j]

    print(pracownicy[i][5], pracownicy[i][24])

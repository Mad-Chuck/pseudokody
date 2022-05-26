def sortowanie(wyraz):
    n = len(wyraz)
    wyraz_list = list(wyraz)

    for i in range(0, n - 1 + 1):
        indeks = i
        for j in range(i + 1, n - 1 + 1):
            if ascii(wyraz_list[j]) < ascii(wyraz_list[indeks]):
                indeks = j
        wyraz_list[i], wyraz_list[indeks] = wyraz_list[indeks], wyraz_list[i]
    return "".join(wyraz_list)

#slowa[0...199][0...4] = wczytaj dane z pliku "anagramy.txt"

with open("anagramy.txt") as f:
     slowa = f.read().splitlines()
     slowa = [i.split() for i in slowa]

for i in range(0, 199 + 1):
    anagram = True
    pierwsze = sortowanie(slowa[i][0])
    for j in range(1, 4 + 1):
        if sortowanie(slowa[i][j]) != pierwsze:
            anagram = False
            break
    if anagram == True:
        print(slowa[i])

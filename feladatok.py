# 1 Írj metódust ami a paraméterben kapott lista elemeit kiírja képernyőre
# 2 Mennyi a pozitiv számok összege? - Összegzés
# 3 Hány negatív szám van? - megszámlálás
# 4 hány tört szám van a számok között? - megszámlálás
# 5 Mennyi a 3-al osztható számok átlaga - összegzés - megszámlálás
# 6 Mekkora a legnagyobb szám? - max
# 7 Mekkora legkisebb szám? - min
# 8 Mekkora a legkisebb és legnagyobb szám különbsége - min, max

# 1
def elsoFeladat(lista):
    index = 0
    while index < len(lista):
        print(lista[index])
        index+=1

def masodikFeladat(lista):
    osszeg = 0
    index = 0
    while index < len(lista):
        if lista[index] > 0:
            osszeg += lista[index]
        index+=1
    return osszeg

def harmadikFeladat(lista):
    szamDb = 0
    index = 0
    while index < len(lista):
        if lista[index] < 0:
            szamDb = szamDb + 1
        index+=1
    return szamDb

def negyedikFeladat(lista):
    szamDb = 0
    index = 0
    while index < len(lista):
        if lista[index] != int(lista[index]):
            szamDb = szamDb + 1
        index+=1
    return szamDb

def otodikFeladat(lista):
    oszto = 0
    osszeg = 0
    index = 0
    while index < len[lista]:
        if lista[index] % 3 == 0:
            osszeg += lista[index]
            oszto += 1
        index+=1
    szam = osszeg / oszto
    return szam

def hatodikFeladat(lista):
    max = 0
    index = 0
    while index < len(lista)-1:
        if lista[index] > max:
            max = lista[index]
        index+=1
    return max

def hetedikFeladat(lista):
    min = 0
    index = 0
    while index < len(lista):
        if lista[index] < min:
            min = lista[index]
        index += 1
    return min

def nyolcadikFeladat(lista):
    min = 0
    max = 0
    index = 0
    while index < len(lista):
        if lista[index] < min:
            min = lista[index]
        if lista[index] > max:
            max = lista[index]
        index += 1
        legnagyobbLegkisebb = max-min
    return legnagyobbLegkisebb







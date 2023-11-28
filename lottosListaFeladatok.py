import math
import random

# 1. Nézzük meg a lottószámok átlagát
# Hány 50-nél nagyobb szám van közte?


def lottoRandomSzamokGenerlasa():
    index = 0
    lista = []
    while index < 5:
        veletlenSzamok = math.floor(random.random()*(101-1)+1)
        lista.append(veletlenSzamok)
        index+=1
    return lista

def LottoSzamokAtlaga(lista):
    db = 0
    osztando = 0
    index = 0
    while index < len(lista):
        db += 1
        osztando += lista[index]
        index+=1
    return osztando / db

def nagyobbEMintOtven(lista):
    megszamlalas = 0
    index = 0
    while index < len(lista):
        if lista[index] > 50:
            megszamlalas = megszamlalas + 1
        index+=1
    return megszamlalas
def legnagyobbSzam(lista):
    max = 0
    index = 0
    while index < len(lista)-1:
        if lista[index] > max:
            max = lista[index]
        index+=1
    return max


def legkisebbSzam(lista):
    min = lista[0]
    index = 0
    while index < len(lista)-1:
        if lista[index] < min:
            min = lista[index]
        index += 1
    return min

def eldontesTetele(lista):
    szamBekeres:int = int(input("Szeretnek kerni egy szamot: "))
    van = 0
    index = 0
    while index < len(lista):
        if lista[index] == szamBekeres:
            van += 1
        index+=1
    return van

def bekeresOtDb(lista):
    index =0
    while index < 5:
        szam = int(input("Szeretnek kerni egy szamot: "))
        if szam not in lista:
            print("Sajnos nem nyert :(")

        index+=1






#Nem megfelelő formatum

#def lottoElsoFeladat(lista):

    # db = 0
    # otvennelNagyobb = 0
    # max = 0
    # min = 0
    # osszeg = 0
    # indexedikElem = 0
    # lista = []
    # #Véletlen szám generálás
    #
    # index = 0
    # while index < 5:
    #     veletlenLottoSzamok = math.floor(random.random()*(101-1)+1)
    #     lista.append(veletlenLottoSzamok)
    #     index+=1
    # index = 0
    # while index < len(lista):
    #     db += 1
    #     osszeg += lista[index]
    # # 2. Hány 50-nél nagyobb szám van közte?
    #     if lista[index] > 50:
    #         otvennelNagyobb += 1
    #     index+=1
    # # 3. Melyik a legnagyobb szám?
    # index = 0
    # while index < len(lista)-1:
    #     if lista[index] > max:
    #         max = lista[index]
    #         indexedikElem = index+1
    #     index+=1
    # # 4. Melyik a legkisebb szám?
    # index = 0
    # while index < len(lista)-1:
    #     if lista[index] < min:
    #         min = lista[index]
    #     index+=1
    #
    #
    # print(f"Ennyi az átlaguk: {osszeg / db}")
    # print(f"Ennyi az 50-el nagyobb: {otvennelNagyobb}")
    # print(f"Legnagyobb szám: {max}")
    # print(f"Legnagyobb szám: {max} Indexedik eleme:  {indexedikElem}")
    # print(f"Legkisebb szám: {min}")








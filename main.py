import lottosListaFeladatok

szamLista = [12,23,-56,82, 12.23, 69, -100]
import feladatok
#feladatok.elsoFeladat(szamLista)
#masodik = feladatok.masodikFeladat(szamLista)
#print(masodik)
#harmadikFeladat = feladatok.harmadikFeladat(szamLista)
#print(harmadikFeladat)
#negyedikFeladat = feladatok.negyedikFeladat(szamLista)
#print(negyedikFeladat)
# otodik = feladatok.otodikFeladat(szamLista)
# print(otodik)
# hatodik = feladatok.hatodikFeladat(szamLista)
# print(hatodik)
# hetedik = feladatok.hetedikFeladat(szamLista)
# print(hetedik)
# 8 feladat
# print(hatodik+hetedik)




# Lottos Feladataok
randomSzamokLista = lottosListaFeladatok.lottoRandomSzamokGenerlasa()
print("Ennyi darab szam egyezik a bekerttel:",lottosListaFeladatok.eldontesTetele(randomSzamokLista),"db")
print("Lista elemei:",randomSzamokLista)
print("Atlaguk",lottosListaFeladatok.LottoSzamokAtlaga(randomSzamokLista))
print("Nagyobb mint 50-en",lottosListaFeladatok.nagyobbEMintOtven(randomSzamokLista))
print("Legnagyobb szám:",lottosListaFeladatok.legnagyobbSzam(randomSzamokLista))
print("Legkisebb szám:",lottosListaFeladatok.legkisebbSzam(randomSzamokLista))
legnagyobbSzam = lottosListaFeladatok.legnagyobbSzam(randomSzamokLista)
legkisebbSzam = lottosListaFeladatok.legkisebbSzam(randomSzamokLista)
print("Legnagyobb - legkisebb",(legnagyobbSzam-legkisebbSzam))
lottosListaFeladatok.bekeresOtDb(randomSzamokLista)
print("Ennyi talaltod volt",lottosListaFeladatok.bekeresOtDbTalalat(randomSzamokLista))

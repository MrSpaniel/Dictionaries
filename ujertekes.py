"""Írj egy programot, amely szótárban tárol adatokat (legalább egy int, str, és bool típusút). A program a írja ki a képernyőre az adatszerkezet! A felhasználónak legyen lehetősége ezt az adatszerkezetet egy kulcs-érték párral bővítenie. A program végül írja ki a képernyőre a frissített adatszerkezetet!"""

adatok = {
    "nev": "Példa", 
    "eletkor": 30,
    "aktiv": "Igen"
}
print("Az adatszerkezet:")
for kulcs, ertek in adatok.items():
    print(f"{kulcs}: {ertek}")

uj_kulcs = input("Kérem adja meg az új kulcsot: ")
uj_ertek = input("Kérem adja meg az új értéket: ")

adatok[uj_kulcs] = uj_ertek

print("A frissített adatszerkezet:")

for kulcs, ertek in adatok.items():
    print(f"{kulcs}: {ertek}")
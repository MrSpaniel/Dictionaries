"""Írj egy programot, amely szótárban tárolja egy macska nevét, korát. A felhasználónak legyen lehetősége megváltoztatni az egyik tárolt adatot. A program írja ki a felhasználó választása alapján az egyik adatot, kérdezze meg, mire módosítsa, végül írja ki a képernyőre a frissített adatszerkezetet!"""

macska = {
    "nev": "Cirmi",
    "kor": 3
}
print("A macska adatai:")
for kulcs, ertek in macska.items():
    print(f"{kulcs}: {ertek}")

valasztas = input("Melyik adatot szeretné megváltoztatni? (nev/kor): ")

if valasztas in macska:

    uj_ertek = input(f"Kérem adja meg az új értéket a(z) {valasztas} számára: ")
    
    if valasztas == "kor":
        uj_ertek = int(uj_ertek)  # Az életkor egész szám legyen
    macska[valasztas] = uj_ertek
    print("A frissített macska adatai:")
    for kulcs, ertek in macska.items():
        print(f"{kulcs}: {ertek}")
else:
    print("Hibás választás! Nincs ilyen adat a szótárban.")
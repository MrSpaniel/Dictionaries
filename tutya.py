"""Írj egy programot, amely a felhasználótól bekéri egy kutya nevét, életkorát, fajtáját, és azt hogy rendelkezik-e érvényes oltással veszettség ellen! Az adatokat tárolja a program szótárban, és írja ki a képernyőre az adatszerkezetet!"""

nev = input("Kérem adja meg a kutya nevét: ")
eletkor = input("Kérem adja meg a kutya életkorát: ")
fajta = input("Kérem adja meg a kutya fajtáját: ")
oltas = input("Rendelkezik-e érvényes oltással veszettség ellen? (igen/nem): ")

kutya = {
    "nev": nev, 
    "eletkor": eletkor,
    "fajta": fajta,
    "oltas": oltas
}

for kulcs, ertek in kutya.items():
    print(f"{kulcs}: {ertek}")
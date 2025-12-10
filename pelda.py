ures_szotar = {}

szemely = {
    "nev": "Kovács János",
    "kor": 25,
    "telefon": "SAMSUNG",
    "varos": "Budapest",
    } 

print(szemely["nev"])
print(szemely["kor"])


print(szemely.get("telefon", "Nincs a szótárban"))

szemely["kor"] = 26
print(szemely["kor"])

szemely["neme"] = "Férfi"
print(szemely.get("neme"))


print(szemely["varos"])
del szemely["varos"]
print(szemely.get("varos", "Nincs a szótárban"))

if "nev" in szemely:
    print("A keresett megtalálható a szótárban.")

if"bankszamla" not in szemely:
    print("A keresett kulcs nem található.")

for kulcs, ertek in szemely.items():
    print(f"{kulcs}, {ertek}")
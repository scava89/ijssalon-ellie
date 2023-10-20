from helper import decoreer

def print_aanbieding():
    prijzen = {
        "aardbei" : int("3"),
        "vanille" : int("4"),
        "chocolade" : int("5")
    }

    aanbieding = prijzen["aardbei"] * 0.8

    reclame_tekst = f"Vandaag in de aanbieding: aarbei-ijs, 1 liter - slechts € {aanbieding}"

    reclame_tekst2 = reclame_tekst[ : -14 ]

    reclame_tekst3 = reclame_tekst2.upper()

    reclame_tekst4 = reclame_tekst3.split()

    for el in reclame_tekst4:
        if (len (el) > 4):
            print(el.upper())
        else:
            print(el.lower())

decoreer("Aanbieding")
print_aanbieding()   
#from algemene_functies import mijn_functie_2

#def aanbieding_1(smaak, prijs, korting):
    
#    korting = prijs * korting
#    korting1 = prijs - korting
#    print(f"vandaag in de aanbieding: emmertje ijs (1 - liter) in de smaak {smaak}, van {prijs} euro voor {korting1} euro")

#aanbieding_1("aardbei", 4, 0.1)

#mijn_lijst = [220,  430, 125, 160, 205, 90, 345]

#def inkomsten_totaal(inkomsten):
    
#    totaal = sum(mijn_lijst)
#    btw = totaal * 0.09
#    print(f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw} euro btw betaald dient te worden")
#inkomsten_totaal("inkomsten")

#def laag_en_hoog(mijn_lijst):
#    print()
#    print(max(mijn_lijst))
#    print()
#    print(min(mijn_lijst))
#    print()
#    return mijn_lijst
#laag_en_hoog(mijn_lijst)
#9
#'''def gemiddelde(mijn_lijst):
#    print(sum(mijn_lijst))

#gemiddelde(mijn_lijst)'''

# 10
#def gemiddelde(mijn_lijst):
#    lengte = len(mijn_lijst)
#    som = sum(mijn_lijst)
#    gemiddelde = som / lengte
#    print(f"De gemiddelde inkomsten deze week zijn {gemiddelde} euro")

#gemiddelde(mijn_lijst)

#extra_lijst = [10, 5, 3, 2, 1, 2, 9]

#def meervoudig(invoer_lijst):
#    laag_en_hoog(invoer_lijst)
#    return invoer_lijst


#def combinatie(invoer_lijst_2):
#    korte_lijst = laag_en_hoog(invoer_lijst_2)
#    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
#    return uitvoer

#combinatie(extra_lijst)
from algemene_functies import mijn_functie_2
def aanbieding_1(smaak, prijs, korting):
    prijs_na_korting = prijs * (1 - korting)
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak} van {prijs} euro voor {prijs_na_korting} euro."
    return uitvoer

def inkomsten_totaal(inkomsten, btw):
    totaal = 0
    for bedrag in inkomsten:
        totaal += bedrag
        btw_bedrag = totaal * btw
        uitvoer = f"Het totaal van alle inkomsten deze week is {totaal} euro, waarover {btw_bedrag} euro btw betaald dient te worden."
        return totaal

dagelijks = [220, 430, 125, 160, 205, 90, 345]

def laag_en_hoog(mijn_lijst):
    uitvoer = []
    laagste = min(mijn_lijst)
    hoogste = max(mijn_lijst)
    uitvoer.append(laagste)
    uitvoer.append(hoogste)
    return uitvoer

def gemiddelde(mijn_lijst):
    aantal = len(mijn_lijst)
    totaal = 0
    for element in mijn_lijst:
        totaal += element
        gemiddelde = totaal / aantal
        return f"De gemiddelde inkomsten van deze week zijn {gemiddelde} in euro."

extra_lijst = [10 , 2, 5, 1, 3, 7, 8, 9]

def meervoudig(invoer_lijst):
    tijdelijk = laag_en_hoog(invoer_lijst)
    uitvoer = tijdelijk[0], tijdelijk[1]
    return uitvoer
print(meervoudig(extra_lijst))


def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer
print(combinatie(extra_lijst))
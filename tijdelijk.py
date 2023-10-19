# 1         ^^^^^^^^
# 2 
prijzen = {
    "aardbei" : int("3"),
    "vanille" : int("4"),
    "chocolade" : int("5")
}
'''aanbieding = float (0.8) * prijzen["aardbei"]
reclame_tekst = (f"Vandaag in de aanbieding : aardbei-ijs, 1 liter - slechts € {aanbieding}")
#print(reclame_tekst)
reclame_tekst2 = reclame_tekst[:-14]
#print(reclame_tekst2)
reclame_tekst3 = reclame_tekst2.upper()
#print(reclame_tekst3)
reclame_tekst4 = reclame_tekst3.split(" ")
#print(reclame_tekst4)
for el in (len) (reclame_tekst4):
    if len < 5:
        print(el.lower())
    else:
        print(el.upper())'''
# 3
aanbieding = float(prijzen["aardbei"]) * 0.8
# 4
reclame_tekst = (f"Vandaag in de aanbieding: aarbei-ijs, 1 liter - slechts € {aanbieding}")
# 5
#print(reclame_tekst)
reclame_tekst2 = reclame_tekst[ : -14 ]
# 6
#print(reclame_tekst2)
reclame_tekst3 = reclame_tekst2.upper()
# 7
#print(reclame_tekst3)
reclame_tekst4 = reclame_tekst3.split()
# 8
#print(reclame_tekst4)
for el in reclame_tekst4:
    if (len (el) > 4):
        print(el.upper())
    else:
        print(el.lower())   
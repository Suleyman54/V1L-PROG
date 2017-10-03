
def split(invoer):
    x = invoer.split('-')
    nieuw_x = []
    for aap in x:
        nieuw_x.append(int(aap))

    groote_waarde = max(x)
    print('het grootste getal is: ' + groote_waarde)

    kleine_waarde = min(x)
    print('Het kleinste getal is: ' + kleine_waarde)

    aantal_getallen = str(len(x))
    print('er zijn: '+ aantal_getallen + ' getallen')

    som_getallen = str(sum(nieuw_x))
    print('totaal: '+ som_getallen)

    berekening = int(som_getallen) / int(aantal_getallen)
    gemiddelde = ('gemiddelde: ' + str(berekening))

    return gemiddelde

print(split("5-9-7-1-7-8-3-2-4-8-7-9"))

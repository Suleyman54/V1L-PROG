def standaardprijs(afstandKM):
    prijs = 0
    if afstandKM > 50:
        prijs = (0.60 * afstandKM + 15)
    else:
        prijs = (0.80 * afstandKM)
    if prijs != 0:
        return(prijs)

def ritprijs(leeftijd, weekendrit, afstandKM):
    prijs = standaardprijs(afstandKM)
    if leeftijd < 12 or leeftijd >= 65:
        if weekendrit == 'false':
            ritprijs = (prijs / 100) * 70
            return ritprijs
        else:
            ritprijs = (prijs / 100) * 65
            return ritprijs
    else:
        if weekendrit == 'true':
            ritprijs = (prijs / 100) * 65
            return ritprijs
        else:
            ritprijs = standaardprijs
    return ritprijs

leeftijd = int(input('wat is je leeftijd'))
weekend = input('Reist u in het weekend: (true or false)')
afstand = int(input('wat is de afstand in km?:'))

print('De prijs voor deze rit bedraagt: €' + str("{0:.2f}".format(ritprijs(leeftijd,weekend,afstand))) + ' euro.')
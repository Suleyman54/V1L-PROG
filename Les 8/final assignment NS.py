def inlezen_beginstation(invoer_stations):
   while True:
       x = str(input('Wat is je beginstation? : '))
       if x in invoer_stations:
           return x

def inlezen_eindstation(invoer_stations, invoer_beginstation):
    indexbegin = invoer_stations.index(invoer_beginstation)
    while True:
        x = str(input('Wat is je eindstation? : '))
        if x in invoer_stations and invoer_stations.index(x) > indexbegin:
            return x

def omroepen_reis(invoer_stations, invoer_beginstation, invoer_eindstation):
    beginrangnummer = invoer_stations.index(invoer_beginstation) + 1
    eindrangnummer = invoer_stations.index(invoer_eindstation) + 1
    afstand = eindrangnummer - beginrangnummer
    bedrag = afstand * 5

    print('Het beginstation ' + str(invoer_beginstation) + ' is het ' + str(beginrangnummer) + 'e station in het traject.')
    print('Het eindstation ' + str(invoer_eindstation) + ' is het ' + str(eindrangnummer) + 'e station in het traject.')
    print('De afstand bedraagt' + str(afstand) + ' station(s).')
    print('De prijs van het kaartje is ' + str(bedrag) + ' euro')
    print('Jij stapt in de trein in: ' + str(invoer_beginstation))

    for x in invoer_stations:
        if invoer_stations.index(x) > beginrangnummer and invoer_stations.index(x) < eindrangnummer:
            print('  -' + str(x))
    print('Jij stapt uit in: ' + str(invoer_eindstation))
stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk','Amsterdam', 'Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', "s-Hertogenbosch", 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht.']

beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)

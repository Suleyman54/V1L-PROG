def gemiddelde():
    zin = input('geef de zin op: ')
    aantal_letters = len(zin) - zin.count(' ')
    aantal_woorden = len(zin.split())

    gemiddelde = str(int(aantal_letters) / int(aantal_woorden))

    print(gemiddelde)

gemiddelde()

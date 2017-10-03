def vierletters():
    strings = input('Voer 10 strings in: ')
    aparte_woorden = strings.split()

    lijst = []

    for x in aparte_woorden:
        tellen = len(x)
        if tellen < 5:
            lijst.append(x)
    print(lijst)


vierletters()
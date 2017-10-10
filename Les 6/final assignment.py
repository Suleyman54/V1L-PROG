def toon_aantal_kluizen_vrij():
    kluizen = open("kluizen.txt")
    print("Er zijn nog " + str(12 - len(kluizen.readlines())) + " Kluizen beschikbaar")


def seperate(toseperate):
    puntcomma = toseperate.find(";")
    nummer = int((toseperate[:puntcomma]))
    wachtwoord = toseperate[puntcomma+1:]
    wachtwoord = wachtwoord[:-1]
    return [nummer, wachtwoord]


def verkrijg_kluizen():
    kluizen = open("kluizen.txt")
    lst = []
    for x in kluizen.readlines():
        lst.append(seperate(x))
    return lst


def nieuwe_kluis():
    kluizen = open("kluizen.txt")
    lst = list(range(1, 13))
    kluisnummers = []

    for kn in kluizen:
        puntcomma = kn.find(";")
        nummer = int((kn[:puntcomma]))
        kluisnummers.append(nummer)

    for a in lst:
        for b in kluisnummers:
            if a == b:
                lst.remove(a)

    if len(lst) >= 0:
        kluizen_append = open("kluizen.txt", "a")
        code = input("\nVoer een code in: ")
        kluizen_append.write("\n" + str(lst[1]) + ";" + str(code))
        print("Jouw kluisnummer is: " + str(lst[1]))
    else:
        print("Er is geen kluisje beschikbaar")


def kluis_openen():
    kluisnummer_openen = eval(input("Wat is jouw kluisnummer? "))
    code_openen = input("Wat is de code? ")
    kluisjes_in_gebruik = verkrijg_kluizen()
    for kluizen in kluisjes_in_gebruik:
        # vergelijken nummers
        if kluizen[0] == kluisnummer_openen:
            # vergelijken wachtwoord
            if kluizen[1] == code_openen:
                print("Gelukt")
                return True
    print("niet gevonden")


def kluis_teruggeven():
    print("Optioneel")


print('''
1: Ik wil weten hoeveel kluizen nog vrij zijn
2: Ik wil een nieuwe kluis
3: Ik wil even iets uit mijn kluis halen
4: Ik geef mijn kluis terug
''')

keuze = input(str("Uw keuze: "))

if keuze == "1":
    toon_aantal_kluizen_vrij()
elif keuze == "2":
    nieuwe_kluis()
elif keuze == "3":
    kluis_openen()
elif keuze == "4":
    kluis_teruggeven()
else:
    print("Dat is geen geldige keuze")
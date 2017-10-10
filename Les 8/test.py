import random


def printDices(dices, role):
    # niet gelijk
    if role == 0:
        print(str(dices[0]) + " + " + str(dices[1]) + " = " + str(sum(dices)))
    elif role==1:
        print(str(dices[0]), " + " , str(dices[1]), " = " , str(sum(dices)) , " (dubbel)")
    elif role==2:
        print(str(dices[0]) + " + " + str(dices[1]) + " = ( ophoepelen)")
    else:
        Exception("YOOOO DIT HOORT NIET")



def intrandom():
    return [random.randrange(1,7), random.randrange(1,7)]



def monopolyworp():
    count = 0
    while True:

        dices = intrandom()
        diceA = dices[0]
        diceB = dices[1]

        if diceA != diceB:
            printDices(dices, 0)
            break
        elif count == 3:
            printDices(dices, 2)
            break
        elif diceA == diceB:
            printDices(dices, 1)
            count += 1
            # 3x op een rij
        else:
            Exception("hier")


monopolyworp()

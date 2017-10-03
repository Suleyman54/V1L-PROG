def seizoen(maandnummer):
    if maandnummer >= 3 and maandnummer <= 5:
        print('Het is lente')
    elif maandnummer >= 6 and maandnummer <= 8:
        print('Het is zomer')
    elif maandnummer >= 9 and maandnummer <= 11:
        print('Het is herfst')
    elif maandnummer >= 1 and maandnummer <=2 or maandnummer == 12:
        print('Het is winter')

seizoen(int(input('Welk maandnummer is het? ')))


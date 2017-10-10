while True:
    x = str(input('geef een woord met vier letters: '))
    if len(x) > 4:
        print(x + ' heeft '+ str(len(x)) + ' letters')
    elif len(x) < 4:
        print(x + ' heeft '+ str(len(x))) + 'letters'
    elif len(x) == 4:
        print('inlezen van correctie sting: ' + x + ' is geslaagd!')
        break




import random

def monopolyworp():
    dobbel1 = random.randrange(1, 7)
    dobbel2 = random.randrange(1, 7)
    dobbel3 = random.randrange(1, 7)
    dobbel4 = random.randrange(1, 7)
    dobbel5 = random.randrange(1, 7)
    dobbel6 = random.randrange(1, 7)
    z = dobbel1 + dobbel2
    b = dobbel3 + dobbel4
    c = dobbel5 + dobbel6
    while True:
        if dobbel1 == dobbel2 and dobbel3 == dobbel4 and dobbel5 == dobbel6:
            print(dobbel1, '+', dobbel2, '=', z)
            print(dobbel3, '+', dobbel4, '=', b)
            print(dobbel5, '+', dobbel6, '= direct naar gevangenis')
            break
        elif dobbel1 == dobbel2 and dobbel3 == dobbel4:
            print(dobbel1, '+', dobbel2, '=', z)
            print(dobbel3, '+', dobbel4, '=', b)
            print(dobbel5, '+', dobbel6, '=', c)
            break
        elif dobbel1 == dobbel2:
            print(dobbel1, '+', dobbel2, '=', z)
            print(dobbel3, '+', dobbel4, '=', b)
            break
        elif dobbel1 != dobbel2:
            print(dobbel1, '+', dobbel2, '=', z)
            break

monopolyworp()
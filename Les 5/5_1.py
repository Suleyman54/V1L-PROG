def convert(celsius):
    celsius = (celsius * 1.8) + 32
    return float(celsius)

def table():
    print('       F          C')
    for celsius in range(-30, 41, 10):
        print('{:10.1f} {:10.1f}'.format(convert(celsius), celsius))

table()

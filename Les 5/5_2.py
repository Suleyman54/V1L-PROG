def test(bestandnaam):
    file = open(bestandnaam)
    c = file.read()
    file.close()
    return c

kaartnummers = test('kaartnummers.txt').splitlines()
for hi in kaartnummers:
    text = hi.split(',')
    print(text[1] + ' heeft kaartnummer ' + text[0])
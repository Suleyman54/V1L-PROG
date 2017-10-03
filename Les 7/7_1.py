# Schrijf een while-loop die steeds getallen van de gebruiker vraagt tot deze 0 ingeeft:

x = []
while True:
    x.append(int(input('geef een getal: ')))
    if x[-1] == 0:
        z = sum(x)
        break

print('Er zijn ' + str(len(x)) + ' getallen ingevoerd, de som is: ' + str(z))

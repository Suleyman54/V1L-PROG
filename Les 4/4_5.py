# grondgetallen = [4, 5, 3, -81]
#
#
# def kwadraten_som(grondgetallen):
#     for x in grondgetallen:
#         if x >= 0:
#             kwadraat = x ** 2
#             print(sum(kwadraat))
# kwadraten_som(grondgetallen)

def kwadraten_som(lijst):
    totaal = 0
    for getal in lijst:
        if getal>0:
            totaal = totaal+getal**2
# kan ook zo getypt worden       totaal+=getal**2
    return(totaal)
print(kwadraten_som([5, 3, 2, -10]))

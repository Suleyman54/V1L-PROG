lengte = float(input('hoe lang ben je? (in meter)'))
gewicht = float(input('Hoe zwaar ben je? (in kg)'))
BMI = gewicht / lengte**2
text = 'je bent te zwaar'
text1 = 'normal'
text3 = 'je bent te dun'
def bmi(BMI):
    if BMI > 25.0:
        return text + " " + str(BMI)
    elif 25.0 > BMI > 18.5:
        return text1 + " " + str(BMI)
    elif BMI < 18.5:
        return text3 + " " + str(BMI)
print(bmi(BMI))
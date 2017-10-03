Lengte = int(input('hoe lang ben jij?'))
def lang_genoeg(Legte):
    if int(Legte >= 120):
        return 'Je bent lang genoeg voor de attractie!'
    else:
        return 'sorry, je bent te klein.'
print(lang_genoeg(Lengte))
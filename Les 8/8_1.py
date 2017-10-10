set_bruin = {'Boxel', 'Best', 'Beukenlaan', 'Eindhoven', "Helmond 't hout", 'Helmond', 'Helmond Brouwhuis', 'Deurne'}
set_groen = {'Boxel', 'Best', 'Beukenlaan', 'Eindhoven', 'Geldrop', 'Heeze', 'Weert'}

print('De overeenkomsten zijn: '+ str(set_bruin.intersection(set_groen)))
print('Het verschil is: ' + str(set_bruin.difference(set_groen)))
print('alle stations samen zijn: ' + str(set_groen.union(set_bruin)))
def leesbestad(naam):
    file = open(naam)
    regels = file.readlines()
    file.close()

    return regels

kaartnummers = leesbestad("kaartnummers.txt")

print("Deze file heeft: " + str(len(kaartnummers)))

hoogstenummers = 0
for huidigregel in kaartnummers:
    woorden = huidigregel.split(', ')
    if int(woorden[0]) > hoogstenummers:
        hoogstenummers = int(woorden[0])

print("Het hoogste kaartnummer is: ", hoogstenummers)

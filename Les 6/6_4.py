studentencijfers = [[95, 92, 86],[66, 75, 54], [89, 72, 100], [34, 0, 0]]

def gemiddelde_per_student(studentencijfers):
    gem = []
    for x in studentencijfers:
        gem.append(sum(x) / len(x))
    return gem
for x in gemiddelde_per_student(studentencijfers):
    print(x)

def gemiddelde_van_alle_studenten(studentencijfers):
    all_grades = gemiddelde_per_student(studentencijfers)
    avg = 0
    for x in all_grades:
        avg += x

    return avg / len(studentencijfers)

print(gemiddelde_van_alle_studenten(studentencijfers))

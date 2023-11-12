def est_bissextile(annee):
    if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):
        return True
    else:
        return False

def annees_bissextiles(siecle):
    annee_debut = (siecle - 1) * 100
    annee_fin = siecle * 100 - 1

    bissextiles = []
    for annee in range(annee_debut, annee_fin + 1):
        if est_bissextile(annee):
            bissextiles.append(annee)

    return bissextiles

siecle = int(input("Saisir le siècle : "))
result = annees_bissextiles(siecle)

print(f"Années bissextiles du siècle {siecle - 1} :")
for annee in result:
    print(annee)

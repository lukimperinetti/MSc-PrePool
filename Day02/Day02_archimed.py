# ----- Archimed ----- #

# π = (4/1) - (4/3) + (4/5) - (4/7) + (4/9) - (4/11) + (4/13) etc etc ...

print('Entrez un nombre. Plus il est élevé, plus le calcul sera précis')
precis = int(input('>>> '))

resultat = 0
denominateur = 1
signe = 1

while precis > 0:
    terme = signe * (4 / denominateur)
    resultat += terme
    denominateur += 2
    signe *= -1
    precis -= 1

print('Le résultat de la somme est :', round(resultat, 6))



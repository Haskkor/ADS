
# Les 4 premiers nombres parfaits connus sont : 6, 28, 496, 8128
# Source : wikipédia

nbr = eval(input("Saisissez un nombre de termes : "))

# Cherche tous les nombres parfaits entre 1 et le nombre choisi
for chiffre in range(1, nbr):
    # Initialise la somme à 0
    somme = 0
    # Parcourt tous les nombres entre 1 et le chiffre en cours
    for ind in range(1, chiffre):
        # Si "ind" est un diviseur du chiffre en cours 
        if chiffre % ind == 0:
            # Ajoute "ind" à la somme
            somme += ind
    # Si la somme est égale au chiffre en cours, le nombre est parfait
    if somme == chiffre:
        print(chiffre)



        

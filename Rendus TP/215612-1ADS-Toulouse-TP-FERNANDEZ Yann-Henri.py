                           #Puissance 4
#2.2 Affichage du plateau
plateau=[["|"]*8 for i in range(6)] # [["|"]]* 7 correspond au nombre de colonne. # For in in range (6) correspond au nombre de ligne # De plus [["|"]] permet de delimiter les colonnes par un "|#
for ligne in plateau:
    for x in ligne:
        print(x,' ',end='')
    print("\n") # Commande de retour a la ligne


# Jusqu'ici nous avons juste affiché un plateau de jeu vide.
x=eval(input("Entrez une valeur comprise entre 1 et 7 inclus : ")) # Entrer une valeur correspondant à l'emplacement voulu sur le plateau de jeu
if x<0 or x>7:
     print("valeur entre 1 et 7 seulement")
else:
    plateau=[["|"]*8 for i in range(6)]
    for ligne in plateau:
        for x in ligne:
            plateau=[["x" for i in range(6)]


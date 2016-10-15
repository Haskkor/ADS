###Fonction prenant en paramètre n retournant liste à n ligne et colonnes


def baseplateau(n,plateau):
    #fonction de mise en place de la liste à deux dimensions
    plateau=[[0 for i in range (n)] for j in range (n)]
    return plateau

###Procédure affichant des valeurs sous forme de plateau d'une liste à 2 dimension


def afficheplateau(plateau):
    for ligne in plateau:
        ligne = map(str, ligne)
        print(' '.join(ligne))
    return plateau




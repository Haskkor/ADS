x = []
y = []
z = []


def test():             # NE FONCTIONNE PAS!
    x = [1, 2, 3]
    y = [4, 5, 6]
    z = [7, 8, 9]
    zipped = zip(x, y, z) # prends valeur de chaque liste separement
    list(zipped)          # PROBLEME AVEC REVERSE
    zipped.reverse()


def rd():                           # rotation sens aiguilles d'une montre
    l = [[1, 2, 3], [4, 5, 6]]
    l.reverse()                     # Nous donne: [[4, 5, 6], [1, 2, 3]]
    zipped2 = zip(*l)               # prend la valeur de chaque sous-liste  # "*":distribue listes presents en arguments
    list(zipped2)                   # nous donne [(4, 1), (5, 2), (6, 3)]. C'EST BON!!!
    print(zipped2)


def test2():                           # rotation sens inverse (rd() 3 fois) NE FONCTIONNE PAS!
    l = [[1, 2, 3], [4, 5, 6]]
    l = l.reverse()                    # 1er rotation
    zipped3 = zip(*l2)
    list(zipped3)
    l3 = zipped3.reverse()              # 2eme rotation
    zipped4 = zip(*l3)
    list(zipped4)
    l4 = zipped4.reverse()              # 3eme rotation
    zipped5 = zip(*l4)
    list(zipped5)
    print(zipped5)


def rg():                               # rotation sens inverse
    l = [[1, 2, 3], [4, 5, 6],[7, 8, 9]]
    m = list(zip(*l))[::-1]             # [::-1] correspond fonction reverse (mettre dans parentheses pour l'autre sens)
    print(m)                            # retourne [(3, 6, 9),(2, 5, 8), (1, 5, 7)] C'EST BON!!!






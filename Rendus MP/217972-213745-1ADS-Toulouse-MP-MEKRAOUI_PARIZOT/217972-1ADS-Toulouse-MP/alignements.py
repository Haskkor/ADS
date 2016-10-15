def alignementH(taille,plateau,win,joueur):
    for i in range(taille):
        cpt=0
        for j in range (taille):
            if plateau[i][j] == joueur:
                cpt+=1
                if cpt == win:
                    return True
            else:
                cpt=0
    return False

def alignementV(taille,plateau,win,joueur):
    for i in range(taille):
        cpt=0
        for j in range (taille):
            if plateau[j][i] == joueur:
                cpt+=1
                if cpt == win:
                    return True
            else:
                cpt=0
    return False

def alignementD1(taille,plateau,win,joueur):
    #diaginferieures
    for i in range(taille):
        cpt=0
        for j in range (taille-i):
            if plateau[taille-j-1][i+j] == joueur:
                cpt+=1
                if cpt == win:
                    return True
            else:
                cpt=0
    #diagsuperieures
    for i in range(taille):
        cpt=0
        for j in range (taille-i):
            if plateau[taille-i-j-1][j] == joueur:
                cpt+=1
                if cpt == win:
                    return True
            else:
                cpt=0
    return False

def alignementD2(taille,plateau,win,joueur):
    #diaginferieures
    for i in range(taille):
        cpt=0
        for j in range (taille-i):
            if plateau[taille-j-1][taille-j-i-1] == joueur:
                cpt+=1
                if cpt == win:
                    return True
            else:
                cpt=0
    #diagsuperieures
    for i in range(taille):
        cpt=0
        for j in range (taille-i):
            if plateau[taille-i-j-1][taille-j-1] == joueur:
                cpt+=1
                if cpt == win:
                    return True
            else:
                cpt=0
    return False

def victoire(taille,plateau,win,joueur):
    if  alignementD2(taille,plateau,win,joueur):
        print("victoire d2",joueur)
        return True
    if  alignementD1(taille,plateau,win,joueur):
        print("victoire d1",joueur)
        return True
    if  alignementV(taille,plateau,win,joueur):
        print("victoire dv",joueur)
        return True
    if  alignementH(taille,plateau,win,joueur):
        print("victoire dh",joueur)
        return True
    return False

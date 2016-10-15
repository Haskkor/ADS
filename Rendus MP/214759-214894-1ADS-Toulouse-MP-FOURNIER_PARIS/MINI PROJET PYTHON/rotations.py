#Variables et plateaux de base


n=6
m=int(n/2)

tampon=[[None for i in range(m)]for j in range(m)]
quadrant=[[None for i in range(m)]for j in range(m)]



#Fonction choisissant un quadrant (liste à 2D) depuis le plateau (liste à 2D) et l'amenant à choisir une rotation horaire ou antihoraire

#Le numéro des cadrants est disposé de telle sorte :

#####
#1#4#
#2#3#
#####



def rotationPlateau(plateau,n,q,v):

    if n%2==0:  #vérification de n pair

        #Quadrant 1

        if q==1:

            if v is True:
                for i in range(m):
                   for j in range(m):
                       quadrant[i][j] = plateau[i][j]
                for i in range(m):
                    for j in range(m):
                        tampon[i][j]=quadrant[m-j-1][i]
                for i in range(m):
                    for j in range(m):
                        plateau[i][j]=tampon[i][j]

            if v is False:
                for i in range(m):
                   for j in range(m):
                       quadrant[i][j] = plateau[i][j]
                for i in range(m):
                    for j in range(m):
                        tampon[i][j]=quadrant[j][m-i-1]
                for i in range(m):
                    for j in range(m):
                        plateau[i][j]=tampon[i][j]

        #Quadrant 2

        if q==2:

            if v is True:

                for i in range(m):
                   for j in range(m):
                       quadrant[i][j] = plateau[i+m][j]
                for i in range(m):
                    for j in range(m):
                        tampon[i][j]=quadrant[m-j-1][i]
                for i in range(m):
                    for j in range(m):
                        plateau[i+m][j]=tampon[i][j]

            if v is False:

                for i in range(m):
                   for j in range(m):
                       quadrant[i][j] = plateau[i+m][j]
                for i in range(m):
                    for j in range(m):
                        tampon[i][j]=quadrant[j][m-i-1]
                for i in range(m):
                    for j in range(m):
                        plateau[i+m][j]=tampon[i][j]

        #Quadrant 3

        if q==3:

            if v is True:
                for i in range(m):
                   for j in range(m):
                       quadrant[i][j] = plateau[i+m][j+m]
                for i in range(m):
                    for j in range(m):
                        tampon[i][j]=quadrant[m-j-1][i]
                for i in range(m):
                    for j in range(m):
                        plateau[i+m][j+m]=tampon[i][j]

            if v is False:
                for i in range(m):
                   for j in range(m):
                       quadrant[i][j] = plateau[i+m][j+m]
                for i in range(m):
                    for j in range(m):
                        tampon[i][j]=quadrant[j][m-i-1]
                for i in range(m):
                    for j in range(m):
                        plateau[i+m][j+m]=tampon[i][j]

        #Quadrant 4

        if q==4:

            if v is True:

                for i in range(m):
                   for j in range(m):
                       quadrant[i][j] = plateau[i][j+m]
                for i in range(m):
                    for j in range(m):
                        tampon[i][j]=quadrant[m-j-1][i]
                for i in range(m):
                    for j in range(m):
                        plateau[i][j+m]=tampon[i][j]

            if v is False:

                for i in range(m):
                   for j in range(m):
                       quadrant[i][j] = plateau[i][j+m]
                for i in range(m):
                    for j in range(m):
                        tampon[i][j]=quadrant[j][m-i-1]
                for i in range(m):
                    for j in range(m):
                        plateau[i][j+m]=tampon[i][j]






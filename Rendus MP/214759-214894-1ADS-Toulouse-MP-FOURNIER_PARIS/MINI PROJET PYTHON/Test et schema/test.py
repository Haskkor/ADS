def affichagePion(plateau,x,y):
    for i in range(n):
        for j in range(n):
            attributionPlacement(i,j,x,y)

            if plateau[i][j]==int(1) :
                maSurface.blit(pionblanc,(x,y))

            elif plateau[i][j]==int(2):
                maSurface.blit(pionnoir,(x,y))


def attributionPlacement(i,j,x,y):
    if i==0:
        y=163
        if j==0:
            x=140
        elif j==1:
            x=218
        elif j==2:
            x=297
        elif j==3:
            x=387
        elif j==4:
            x=465
        elif j==5:
            x=547

    elif i==1:
        y=249
        if j==0:
             x=140
        elif j==1:
            x=218
        elif j==2:
            x=297
        elif j==3:
            x=387
        elif j==4:
            x=465
        elif j==5:
            x=547

    elif i==2:
        y=320
        if j==0:
            x=140
        elif j==1:
            x=218
        elif j==2:
            x=297
        elif j==3:
            x=387
        elif j==4:
            x=465
        elif j==5:
            x=547

    elif i==3:
        y=412
        if j==0:
            x=140
        elif j==1:
            x=218
        elif j==2:
            x=297
        elif j==3:
            x=387
        elif j==4:
            x=465
        elif j==5:
            x=547

    elif i==4:
        y=489
        if j==0:
            x=140
        elif j==1:
            x=218
        elif j==2:
            x=297
        elif j==3:
            x=387
        elif j==4:
            x=465
        elif j==5:
            x=547

    elif i==5:
        y=572
        if j==0:
            x=140
        elif j==1:
            x=218
        elif j==2:
            x=297
        elif j==3:
            x=387
        elif j==4:
            x=465
        elif j==5:
            x=547
    return x and y


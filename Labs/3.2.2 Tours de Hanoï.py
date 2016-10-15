import os

def hanoi(n, A = "A", B = "B", C = "C"):
    #print(A,B,C)
    if n > 0:
        hanoi(n - 1, A, C, B)
        print("Deplace " + A + " sur " + C)
        hanoi(n - 1, B, A, C)

n = eval(input("Nombre de disques : "))
hanoi(n)

os.system("pause")

##Nous disposons de trois tours A, B et C. Deux disques sont sur A, les tours de départ et B
##et C sont vides. Comment s'y prendre pour déplacer tous les disques de A vers C en passant
##par B ?
##
##Nous savons que sur la tour A, le plus grand disque se situe sous le second, qui est
##forcément plus petit. Or, nous devons parvenir à un résultat tel que ce plus grand disque
##se trouve à la base de la tour C et le second, plus petit, au sommet de la tour C et
##malheureusement, nous sommes contraints de ne déplacer qu'un disque à la fois et toujours de
##sommet vers sommet. La première opération à faire est donc de dégager le plus petit disque
##(le sommet de la tour A) et de le placer dans la tour B. On peut ensuite aisément déplacer
##la base de la tour A, le plus grand disque, vers la base de la tour C. Puis il suffit de
##retirer le petit disque de la tour B et de le placer au sommet de la tour C. Au final, on a
##déplacé tous les disques de la tour A vers la tour C, le problème a été résolu correctement.
##
##Il faut penser récursivement. Pour résoudre le problème des tours de Hanoï avec deux disques,
##on a déplacé de A vers B, puis de A vers C pour finalement déplacer de B vers C (une seule et
##unique opération est à chaque fois possible). Donc (2-1) disque de A vers B, puis 1 disques
##(le plus grand) de A vers C et à la fin (2-1) disque de B vers C. La logique est donc la
##suivante : "isoler le plus grand disque de A puis le placer à la base de la tour de
##destination C puis appliquer le même algorithme de B vers C". En résumé, l'algorithme de
##résolution des tours de Hanoï sur un nombre n de disques est le suivant :
##
##Déplacer n disques de A vers C en passant par B :
##Déplacer (n-1) disques de A vers B en passant par C;
##Déplacer 1 disque de A vers C ;
##Déplacer (n-1) disques de B vers C en passant par A.

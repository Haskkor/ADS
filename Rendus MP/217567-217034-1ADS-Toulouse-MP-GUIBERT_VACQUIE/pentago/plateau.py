#opérations sur la table
   

def convert(liste):
    #Renvoie une table à deux dimensions [ligne][colonne] à partir de la table à cadrants
        
        tampon=[["","","","","",""],["","","","","",""],["","","","","",""],["","","","","",""],["","","","","",""],["","","","","",""]]
    
        for v in range(0,6):
                for w in range(0,6):
                        
                        if w<3 and v<3:
                                tampon[v][w]=liste[0][v][w]
                        if w>=3 and v<3:
                                tampon[v][w]=liste[1][v][w-3]
                        if w<3 and v>=3:
                                tampon[v][w]=liste[2][v-3][w]
                        if w>=3 and v>=3:
                                tampon[v][w]=liste[3][v-3][w-3]
		    			
        return tampon


def rotate(liste,cadrant,sens):
        #tourne un cadrant un sens
        #sens trigo=1
        #sens anti trigo=0
        global table
	
        if sens==1:
            a=3
        elif sens==0:
            a=1
	
        for i in range(0,a):
            tampon=[["","",""],["","",""],["","",""]]
            tampon[0][0]=liste[cadrant][2][0]
            tampon[2][0]=liste[cadrant][2][2]
            tampon[2][2]=liste[cadrant][0][2]
            tampon[0][2]=liste[cadrant][0][0]
		
            tampon[0][1]=liste[cadrant][1][0]
            tampon[1][0]=liste[cadrant][2][1]
            tampon[2][1]=liste[cadrant][1][2]
            tampon[1][2]=liste[cadrant][0][1]
		
            tampon[1][1]=liste[cadrant][1][1]
            
            table[cadrant]=tampon
  

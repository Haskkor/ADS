
#Excusez moi j'ai eu des soucis avec pygame du coup jai pris un alternatif et jai utilisé tkinter.


from tkinter import *

main = Tk()     # on crée la fenetre principale de notre interface
main.geometry("800x700")                                                # on définie les dimensions
main.title("PENTAGO")                                                   # titre en haut de la fenetre
main['bg'] = '#7161C1'                                                  # couleur de fond violet
champ_label = Label(main, text = "Bienvenue sur Pentago", fg = '#000000', bg = '#7161C1' )               # ligne de texte souhaitant bienvenue
champ_label.pack(fill="both")                                                                                 # on affiche le texte
bouton_quitter = Button(main, text="QUITTER", fg = 'red', command = main.quit)                     # bouton pour quitter le jeu
bouton_quitter.place(rely = 1.0, relx = 0, anchor = SW)                            # rely=1 signifie la bas; relx=1 a droite
bouton_continuer = Button(main, text="CONTINUER", fg='red')                                      # mettre commande qui ouvre le plateau
bouton_continuer.place(rely = 1.0, relx = 1.0, anchor = SE)



main.mainloop()                                                                                 # démarre la boucle tkinter jusqu'a fermeture de la fenetre


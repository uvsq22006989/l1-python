
import tkinter as tk
import random
"""racine = tk.Tk()
racine.title("Mon dessin")
# création des widgets
bouton_cercle = tk.Button(racine, text="Cercle")
bouton_carre = tk.Button(racine, text="Carré")
bouton_croix = tk.Button(racine, text="Croix")
bouton_couleur = tk.Button(racine, text="Choisir une couleur")
canvas = tk.Canvas(racine, width=500, height=500, bg="black")
# placement des widgets
bouton_cercle.grid(column=0, row=1)
bouton_carre.grid(column=0, row=2)
bouton_croix.grid(column=0, row=3)
bouton_couleur.grid(column=1, row=0)
canvas.grid(column=1, row=1, rowspan=3)
racine.mainloop()"""


HEIGHT = 500
WIDTH = 500
Taille=100
paint="cyan"
couleur=["blue","red","yellow","grey"]
racine = tk.Tk() # Création de la fenêtre racine
canvas = tk.Canvas(racine, bg="grey", height=HEIGHT, width=WIDTH)
# on récupère l'identifiant du cercle:
for loop in range(2):
    canvas.grid(column=0, row=0)
    cercle = canvas.create_oval((100, 100), (300, 300), fill=couleur, width=Taille, outline=paint) 
    Taille-1
    b=randomint(0,3)
    paint=couleur[b]
    
racine.mainloop() # Lancement de la boucle principale




import tkinter as tk
import math


class Calculatrice:
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.fenetre.title("Calculatrice")

        self.affichage_var = tk.StringVar()
        self.affichage_var.set("")

        self.creer_interface()

    def creer_interface(self):
        # Zone d'affichage de la calculatrice avec un style personnalisé
        self.affichage = tk.Entry(self.fenetre, textvariable=self.affichage_var, font=("Helvetica", 24),
                                  justify="right", bd=10, insertbackground="white")
        self.affichage.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=8, ipady=8)

        # Liste des boutons numériques et opérateurs
        boutons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '+'
        ]

        row = 1
        col = 0
        for bouton_texte in boutons:
            # Création et placement des boutons dans la grille avec un style personnalisé
            bouton = tk.Button(self.fenetre, text=bouton_texte, font=("Helvetica", 18), padx=20, pady=20, bd=6,
                               command=lambda texte=bouton_texte: self.bouton_appuye(texte))
            bouton.grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        # Bouton "C" pour effacer l'affichage avec un style personnalisé
        tk.Button(self.fenetre, text="C", font=("Helvetica", 18), padx=20, pady=20, bd=6,
                  command=lambda: self.mettre_a_jour_affichage("")).grid(row=row, column=col)
        # Bouton "=" pour calculer le résultat avec un style personnalisé
        tk.Button(self.fenetre, text="=", font=("Helvetica", 18), padx=20, pady=20, bd=6, command=self.calculer).grid(
            row=row + 1, column=col)

    def mettre_a_jour_affichage(self, texte):
        # Met à jour l'affichage de la calculatrice
        self.affichage_var.set(texte)

    def bouton_appuye(self, caractere):
        # Gère l'appui sur les boutons numériques et opérateurs
        affichage_actuel = self.affichage_var.get()
        self.mettre_a_jour_affichage(affichage_actuel + caractere)

    def calculer(self):
        # Évalue l'expression mathématique et affiche le résultat
        try:
            expression = self.affichage_var.get()
            resultat = str(eval(expression))
            self.mettre_a_jour_affichage(resultat)
        except Exception as e:
            self.mettre_a_jour_affichage("Erreur")


if __name__ == "__main__":
    fenetre = tk.Tk()
    app = Calculatrice(fenetre)
    fenetre.mainloop()

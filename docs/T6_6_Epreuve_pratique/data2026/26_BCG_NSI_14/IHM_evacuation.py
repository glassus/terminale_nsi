from simulation_evacuation import Piece, evacuation
from tkinter import *
from random import randint

################################################################################
# Il n'est pas nécessaire de comprendre (ni modifier) le code de ce programme. #
# Son execution ouvre une interface graphique qui facilitera vos tests.        #
################################################################################


def creation_piece():
    global choix_largeur, choix_profondeur, choix_nboccupants, piece_test
    global dessin, dernier_affichage, nb_tour_evac
    piece_test = Piece(choix_profondeur.get(), choix_largeur.get())
    n = min(choix_nboccupants.get(), piece_test.capacite)
    while n > 0:
        i = randint(0, piece_test.i_max)
        j = randint(0, piece_test.j_max)
        nb = piece_test.ajouter_occupants(i, j, randint(1, min(5, n)))
        n = n - nb
    dernier_affichage = [[[None, None] for _ in range(
        piece_test.j_max + 1)] for _ in range(piece_test.i_max + 1)]
    dessin.delete(ALL)
    nb_tour_evac.configure(text="")


def affichage_grille():
    global piece_test, dessin, mode_daltonien, dernier_affichage, nb_occ_restants
    if piece_test is not None:
        couleurs = ["white", "blue", "green", "yellow", "orange", "red"]
        for (lg, cl) in piece_test.sorties:
            if lg == 0:
                dessin.create_text(15*cl+22, 7, text="P")
            elif cl == 0:
                dessin.create_text(7, 15*lg+22, text="P")
            elif lg == piece_test.i_max:
                dessin.create_text(15*cl+22, 15*lg+37, text="P")
            else:
                dessin.create_text(15*cl+37, 15*lg+22, text="P")
        for lg in range(piece_test.i_max + 1):
            for cl in range(piece_test.j_max + 1):
                nb = piece_test.grille[lg][cl]
                case = dernier_affichage[lg][cl]
                if case[0] is None:
                    case[0] = dessin.create_rectangle(
                        15*cl+15, 15*lg+15, 15*cl+30, 15*lg+30, fill="white")
                if case[1] is None:
                    case[1] = dessin.create_text(15*cl+22, 15*lg+22, text="")
                if dessin.itemcget(case[0], "fill") != couleurs[nb]:
                    dessin.itemconfig(case[0], fill=couleurs[nb])
                if mode_daltonien.get() == "oui" and dessin.itemcget(case[1], "text") != str(nb):
                    dessin.itemconfig(case[1], text=str(nb))
                if mode_daltonien.get() == "non" and dessin.itemcget(case[1], "text") != "":
                    dessin.itemconfig(case[1], text="")
        nb_occ_restants.configure(text=str(piece_test.nb_occupants_restants()))
    dessin.after(100, affichage_grille)


def clic_gauche(event):
    global piece_test
    if piece_test is not None:
        cl, lg = event.x // 15, event.y // 15
        if lg == 0:
            # ajout d'une sortie au nord
            piece_test.ajouter_sortie("N", min(cl-1, piece_test.j_max))
        elif cl == 0:
            # ajout d'une sortie à l'ouest
            piece_test.ajouter_sortie("O", min(lg-1, piece_test.i_max))
        elif lg > piece_test.i_max:
            # ajout d'une sortie au sud
            piece_test.ajouter_sortie("S", min(cl-1, piece_test.j_max))
        elif cl > piece_test.j_max:
            # ajout d'une sortie à l'est
            piece_test.ajouter_sortie("E", min(lg-1, piece_test.i_max))
        else:
            # ajout d'occupants
            piece_test.ajouter_occupants(lg-1, cl-1, 5)


def alerter_occupants():
    global piece_test
    if piece_test is not None and piece_test.sorties != []:
        nb_tour_evac.configure(text="")
        piece_test.alerter()


def evacuer_occupants():
    global piece_test, nb_tour_evac
    if piece_test is not None and piece_test.sorties != []:
        nbT = evacuation(piece_test)
        if piece_test.nb_occupants_restants() == 0:
            nb_tour_evac.configure(
                text="Evacuation effectuée en " + str(nbT) + " tours.")
        else:
            nb_tour_evac.configure(text="Echec de l'évacuation.")


if __name__ == "__main__":
    global fen, choix_largeur, choix_profondeur, choix_nboccupants
    global piece_test, dessin, mode_daltonien, nb_occ_restants, nb_tour_evac
    piece_test = None
    # création de la fenêtre
    fen = Tk()
    fen.title("IHM de simulation d'évacuation")
    fen.geometry("430x650")
    # ajout des zones de saisie permettant de paramétrer la simulation
    Label(fen, text="Largeur de la pièce").grid(row=1, column=1, columnspan=2)
    choix_largeur = Scale(fen, from_=10, to=20, orient=HORIZONTAL)
    choix_largeur.set(10)
    choix_largeur.grid(row=1, column=3)
    Label(fen, text="Profondeur de la pièce").grid(
        row=2, column=1, columnspan=2)
    choix_profondeur = Scale(fen, from_=10, to=20, orient=HORIZONTAL)
    choix_profondeur.set(10)
    choix_profondeur.grid(row=2, column=3)
    Label(fen, text="Nombre d'occupants placés aléatoirement \n(dans la limite de capacité de la pièce)").grid(
        row=3, column=1, columnspan=2)
    choix_nboccupants = Scale(fen, from_=10, to=2000, orient=HORIZONTAL)
    choix_nboccupants.set(200)
    choix_nboccupants.grid(row=3, column=3)
    Label(fen, text="Affichage des nombres en plus des couleurs \n (mode daltonien)").grid(
        row=4, column=1, columnspan=2)
    mode_daltonien = StringVar()
    Checkbutton(fen, text="", var=mode_daltonien, onvalue="oui",
                offvalue="non").grid(row=4, column=3)
    mode_daltonien.set("non")
    btn_grille = Button(fen, text="Créer la pièce", command=creation_piece)
    btn_grille.grid(row=5, column=2)
    # ajout du canvas où sera dessinée la pièce
    Label(fen, text="Un clic sur un côté de la pièce permet d'ajouter une sortie. \nPour ajouter des occupants, cliquer dans la pièce.").grid(
        row=6, column=1, columnspan=3)
    dessin = Canvas(fen, bg="grey", height=330, width=330)
    dessin.grid(row=7, column=1, columnspan=3)
    dessin.bind("<Button-1>", clic_gauche)
    dessin.after(100, affichage_grille)
    Label(fen, text="Nombre d'occupants actuellement dans la pièce :").grid(
        row=8, column=1, columnspan=2)
    nb_occ_restants = Label(fen, text="")
    nb_occ_restants.grid(row=8, column=3)
    # ajout des boutons d'alerte et d'évacuation
    btn_alerte = Button(
        fen, text="Alerter (un pas vers la sortie la plus proche)", command=alerter_occupants)
    btn_alerte.grid(row=9, column=1, columnspan=2)
    btn_evacuer = Button(fen, text="Evacuer", command=evacuer_occupants)
    btn_evacuer.grid(row=9, column=3)
    nb_tour_evac = Label(fen, text="")
    nb_tour_evac.grid(row=10, column=1, columnspan=3)
    # affichage de la fenêtre
    fen.mainloop()
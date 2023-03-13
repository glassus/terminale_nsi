# Exercices de programmation dynamique

## Exercice 1

Exercice 5 du sujet [Métropole J2 2022](https://glassus.github.io/terminale_nsi/T6_Annales/data/2022/2022_Metropole_J2.pdf){. target="_blank"}

??? tip "Correction Q1."
    ```python
    cellule = Cellule(True, False, True, True)
    ```

??? tip "Correction Q2."
    ```python linenums='1' hl_lines='7 9-11'
    class Labyrinthe:
        def __init__(self, hauteur, longueur):
            self.grille = self.construire_grille(hauteur, longueur)

        def construire_grille(self, hauteur, longueur):
            grille = []
            for i in range(hauteur):
                ligne = []
                for j in range(longueur):
                    cellule = Cellule(True, True, True, True)
                    ligne.append(cellule)
                grille.append(ligne)
            return grille
    ```

??? tip "Correction Q3."
    ```python
    cellule2.murs['S'] = False
    ```

??? tip "Correction Q4."
    ```python
    elif c1_lig == c2_lig and c1_col - c2_col == 1:
        cellule1.murs['O'] = False
        cellule2.murs['E'] = False
    ```

??? tip "Correction Q5."
    ```python linenums='1' hl_lines='3 6 7'
    def creer_labyrinthe(self, ligne, colonne, haut, long):
        if haut == 1 : # Cas de base
            for k in range(colonne, colonne + long - 1):
                self.creer_passage(ligne, k, ligne, k + 1)
        elif long == 1: # Cas de base
            for k in range(ligne, ligne + haut - 1):
                self.creer_passage(k, colonne, k + 1, colonne)
        else: # Appels récursifs
                # Code non étudié (Ne pas compléter)
    ```

??? tip "Correction Q6."
    ![image](data/exo5.png){: .center}
    
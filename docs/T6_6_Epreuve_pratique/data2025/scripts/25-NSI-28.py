def voisinage(n, ligne, colonne):
    """ Renvoie la liste des coordonnées des voisins de la case
    (ligne, colonne) dans un grille de taille n x n,
    en tenant compte des cases sur les bords. """
    voisins = []
    for dl in range(-1, 2):
        for dc in range(-1, 2):
            l = ligne + dl
            c = colonne + dc
            if (l, c) != (ligne, colonne) \
                    and 0 <= l < n and 0 <= c < n:
                voisins.append((l,c))
    return voisins

def incremente_voisins(grille, ligne, colonne):
    """ Incrémente de 1 toutes les cases voisines d'une bombe."""
    voisins = ... 
    for l, c in voisins:
        if grille[l][c] != ...: # si ce n'est pas une bombe 
            ...  # on ajoute 1 à sa valeur 

def genere_grille(bombes):
    """ Renvoie une grille de démineur de taille nxn où n est
    le nombre de bombes, en plaçant les bombes à l'aide de
    la liste bombes de coordonnées (tuples) passée en
    paramètre. """
    n = len(bombes)
    # Initialisation d'une grille nxn remplie de 0
    grille = [[0 for colonne in range(n)] for ligne in range(n)]
    # Place les bombes et calcule les valeurs des autres cases
    for ligne, colonne in bombes:
        grille[ligne][colonne] = ... # place la bombe 
        ...  # incrémente ses voisins 
    return grille



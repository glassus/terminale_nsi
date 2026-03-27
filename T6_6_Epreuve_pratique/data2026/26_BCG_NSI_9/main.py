from Objet3D import Objet3D

#############################################################################
# Variables et fonctions fournies pour la question 3                        #
#############################################################################
parametres_imprimante = {'remplissage': 20,
                         'vitesse_extrusion': 8}  # 8mm3 / seconde


def volume_cube(cube):
    a, b = cube.sommets_adjacents()
    taille_cote = a.distance(b)  # distance donnee en mm
    return taille_cote ** 3

#############################################################################
# Écrire le code de la fonction estimation_impression de la question 3      #
#############################################################################


#############################################################################
# Programme à modifier de la question 4 et 5                                #
#############################################################################
objet = Objet3D()
objet.ajouter_sommet(0, 0, 0)
objet.ajouter_sommet(0, 1, 0)
objet.ajouter_sommet(1, 1, 0)
objet.ajouter_sommet(1, 0, 0)
objet.ajouter_face([1, 2, 3, 4])
objet.afficher()
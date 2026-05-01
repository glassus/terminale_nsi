from Objet3D import Objet3D

#############################################################################
# Variables et fonctions fournies pour la question 3                        #
#############################################################################


class Imprimante3D:
    def __init__(self, remplissage, vitesse_extrusion):
        self.remplissage = remplissage
        self.vitesse_extrusion = vitesse_extrusion

    #############################################################################
    #  Écrire le code de la méthode estimation_impression de la question 3      #
    #############################################################################

    def estimation_impression(self, objet):
        pass


rhombi = Objet3D()

# Définition des 24 sommets
rhombi.ajouter_sommet(1, 1, 3)    # s0
rhombi.ajouter_sommet(1, 1, -3)   # s1
rhombi.ajouter_sommet(1, -1, 3)   # s2
rhombi.ajouter_sommet(1, -1, -3)  # s3
rhombi.ajouter_sommet(-1, 1, 3)   # s4
rhombi.ajouter_sommet(-1, 1, -3)  # s5
rhombi.ajouter_sommet(-1, -1, 3)  # s6
rhombi.ajouter_sommet(-1, -1, -3)  # s7
rhombi.ajouter_sommet(1, 3, 1)    # s8
rhombi.ajouter_sommet(1, 3, -1)   # s9
rhombi.ajouter_sommet(1, -3, 1)   # s10
rhombi.ajouter_sommet(1, -3, -1)  # s11
rhombi.ajouter_sommet(-1, 3, 1)   # s12
rhombi.ajouter_sommet(-1, 3, -1)  # s13
rhombi.ajouter_sommet(-1, -3, 1)  # s14
rhombi.ajouter_sommet(-1, -3, -1)  # s15
rhombi.ajouter_sommet(3, 1, 1)    # s16
rhombi.ajouter_sommet(3, 1, -1)   # s17
rhombi.ajouter_sommet(3, -1, 1)   # s18
rhombi.ajouter_sommet(3, -1, -1)  # s19
rhombi.ajouter_sommet(-3, 1, 1)   # s20
rhombi.ajouter_sommet(-3, 1, -1)  # s21
rhombi.ajouter_sommet(-3, -1, 1)  # s22
rhombi.ajouter_sommet(-3, -1, -1)  # s23

# Faces carrées principales (axiales)
rhombi.ajouter_face([0, 2, 6, 4])     # Z+
rhombi.ajouter_face([1, 5, 7, 3])     # Z-
rhombi.ajouter_face([16, 17, 19, 18])  # X+
rhombi.ajouter_face([20, 22, 23, 21])  # X-
rhombi.ajouter_face([8, 12, 13, 9])   # Y+
rhombi.ajouter_face([10, 11, 15, 14])  # Y-

# Faces carrées de jonction (arêtes)
rhombi.ajouter_face([0, 16, 18, 2])   # Z+/X+
rhombi.ajouter_face([4, 6, 22, 20])   # Z+/X-
rhombi.ajouter_face([1, 3, 19, 17])   # Z-/X+
rhombi.ajouter_face([5, 21, 23, 7])   # Z-/X-
rhombi.ajouter_face([0, 4, 12, 8])    # Z+/Y+
rhombi.ajouter_face([2, 10, 14, 6])   # Z+/Y-
rhombi.ajouter_face([1, 9, 13, 5])    # Z-/Y+
rhombi.ajouter_face([3, 7, 15, 11])   # Z-/Y-
rhombi.ajouter_face([8, 16, 17, 9])   # Y+/X+
rhombi.ajouter_face([12, 20, 21, 13])  # Y+/X-
rhombi.ajouter_face([10, 18, 19, 11])  # Y-/X+
rhombi.ajouter_face([14, 22, 23, 15])  # Y-/X-

# Faces triangulaires (sommets)
rhombi.ajouter_face([0, 8, 16])  # X+Y+Z+
rhombi.ajouter_face([4, 12, 20])  # X-Y+Z+
rhombi.ajouter_face([2, 10, 18])  # X+Y-Z+
rhombi.ajouter_face([6, 14, 22])  # X-Y-Z+
rhombi.ajouter_face([1, 17, 9])  # X+Y+Z-
rhombi.ajouter_face([5, 13, 21])  # X-Y+Z-
rhombi.ajouter_face([3, 19, 11])  # X+Y-Z-
rhombi.ajouter_face([7, 15, 23])  # X-Y-Z-

# rhombi.afficher() # à décommenter pour afficher le rhombicuboctaèdre

imprimante = Imprimante3D(20, 1.2)
print(imprimante.estimation_impression(rhombi))

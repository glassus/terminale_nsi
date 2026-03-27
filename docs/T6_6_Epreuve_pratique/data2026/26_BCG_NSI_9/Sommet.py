import math


class Sommet:

    """
    Représente un sommet (point) dans l'espace 3D.
    """

    def __init__(self, x, y, z):
        """
        Initialise un sommet avec ses coordonnées.
        """
        self.x = x
        self.y = y
        self.z = z

    def est_adjacent(self, sommet):
        """
        Indique si le sommet courant est adjacent à un autre sommet.
        """
        nb_changement = 0
        if self.x != sommet.x:
            nb_changement = nb_changement + 1
        if self.y != sommet.y:
            nb_changement = nb_changement + 1
        if self.z != sommet.z:
            nb_changement = nb_changement + 1
        return nb_changement == 1


#############################################################################
# Écrire le code de la méthode distance de la question 1                    #
#############################################################################

#############################################################################
# Programme pour tester votre méthode de la question 1                                  #
#############################################################################
s1 = Sommet(0, 0, 0)
s2 = Sommet(3, 4, 0)
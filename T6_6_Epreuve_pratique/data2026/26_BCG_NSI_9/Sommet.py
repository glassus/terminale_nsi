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

    #############################################################################
    # Écrire le code de la méthode distance de la question 1                    #
    #############################################################################

    def distance(self, s):
        return ((s.x-self.x)**2+(s.y-self.y)**2+(s.z-self.z)**2)**0.5


#############################################################################
# Programme pour tester votre méthode de la question 1                      #
#############################################################################
s1 = Sommet(0, 0, 0)
s2 = Sommet(3, 4, 0)

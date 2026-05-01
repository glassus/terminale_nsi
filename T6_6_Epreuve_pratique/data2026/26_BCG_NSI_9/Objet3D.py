from Sommet import Sommet
from Face import Face
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


class Objet3D:

    """
    Représente un objet 3D composé de sommets, de faces et d'un nom.
    """

    def __init__(self):
        """
        Initialise un objet 3D vide.
        """
        self.sommets = []
        self.faces = []
        self.nom = ""

    def ajouter_sommet(self, x, y, z):
        """
        Ajoute un sommet à l'objet 3D.
        """
        self.sommets.append(Sommet(x, y, z))

    def ajouter_face(self, liste_sommets):
        """
        Ajoute une face à l'objet 3D.
        """
        self.faces.append(Face([self.sommets[i] for i in liste_sommets]))

    def __str__(self):
        """
        Renvoie une représentation textuelle de l'objet 3D.
        """
        return str({'nom': self.nom, 'sommets': len(self.sommets), 'faces': len(self.faces)})

    def afficher(self):
        """
        Affiche l'objet 3D à l'aide de matplotlib.
        """
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        f = []
        for face in self.faces:
            x = [(s.x, s.y, s.z) for s in face.sommets]
            f.append(x)
        mesh = Poly3DCollection(f, alpha=0.4, edgecolor='black')
        ax.add_collection3d(mesh)
        plt.show()

    #############################################################################
    # Méthode à modifier de la question 5                                       #
    #############################################################################
    def transformer(self, rapport):
        """
        Applique une transformation d'échelle à l'objet 3D en modifiant directement ses sommets.
        """
        sommets = []
        for sommet in self.sommets:
            sommets.append(
                Sommet(sommet.x * rapport,
                       sommet.y * rapport, sommet.z * rapport))
        self.sommets = sommets

    #############################################################################
    # Écrire le code de la méthode sommets_adjacents de la question 2           #
    #############################################################################

    def sommets_adjacents(self, s1, s2):
        pass

    def longueur_plus_longue_arete(self):
        max_longueur = 0
        for s1 in self.sommets:
            for s2 in self.sommets:
                if self.sommets_adjacents(s1, s2):
                    d = s1.distance(s2)
                    if d > max_longueur:
                        max_longueur = d
        return max_longueur

    def volume_cube_englobant(self):
        longueur_max = self.longueur_plus_longue_arete()
        return longueur_max ** 3


#############################################################################
# Cube pour tester votre méthode de la question 2                           #
#############################################################################

cube = Objet3D()
cube.ajouter_sommet(0, 0, 0)  # s0
cube.ajouter_sommet(1, 2, 2)  # s1
cube.ajouter_sommet(3, 3, 0)  # s2
cube.ajouter_sommet(2, 1, -2)  # s3
cube.ajouter_sommet(-2, 2, -1)  # s4
cube.ajouter_sommet(-1, 4, 1)  # s5
cube.ajouter_sommet(1, 5, -1)  # s6
cube.ajouter_sommet(0, 3, -3)  # s7
cube.ajouter_face([0, 1, 2, 3])
cube.ajouter_face([4, 5, 6, 7])
cube.ajouter_face([0, 1, 5, 4])
cube.ajouter_face([1, 2, 6, 5])
cube.ajouter_face([2, 3, 7, 6])
cube.ajouter_face([3, 0, 4, 7])
# cube.afficher() # à décommenter pour afficher le cube en 3d

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
        self.faces.append(Face(liste_sommets))

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
            print(face.sommets)
            x = [(self.sommets[s-1].x, self.sommets[s-1].y, self.sommets[s-1].z)
                 for s in face.sommets]
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
                Sommet(sommet.x*rapport, sommet.y*rapport, sommet.z*rapport))
        self.sommet = sommets


#############################################################################
# Écrire le code de la méthode trouver_sommets_adjacents de la question 2   #
#############################################################################


#############################################################################
# Programme pour tester votre méthode de la question 2                                  #
#############################################################################
objet = Objet3D()
objet.ajouter_sommet(0, 0, 0)  # s1
objet.ajouter_sommet(1, 0, 0)  # s2
objet.ajouter_sommet(0, 1, 0)  # s3
objet.ajouter_sommet(0, 0, 1)  # s4
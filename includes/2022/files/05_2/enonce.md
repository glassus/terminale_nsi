On dispose d’un programme permettant de créer un objet de type `PaquetDeCarte`,
selon les éléments indiqués dans le code ci-dessous.
Compléter ce code aux endroits indiqués par `#A compléter`, puis ajouter des
assertions dans l’initialiseur de `Carte`, ainsi que dans la méthode `getCarteAt()`.

```python linenums='1'
class Carte:
    """Initialise Couleur (entre 1 a 4), et Valeur (entre 1 a 13)"""
    def __init__(self, c, v):
        self.Couleur = c
        self.Valeur = v

    """Renvoie le nom de la Carte As, 2, ... 10, 
       Valet, Dame, Roi"""
    def getNom(self):
        if ( self.Valeur > 1 and self.Valeur < 11):
            return str( self.Valeur)
        elif self.Valeur == 11:
            return "Valet"
        elif self.Valeur == 12:
            return "Dame"
        elif self.Valeur == 13:
            return "Roi"
        else:
            return "As"

    """Renvoie la couleur de la Carte (parmi pique, coeur, carreau, trefle"""
    def getCouleur(self):
        return ['pique', 'coeur', 'carreau', 'trefle' ][self.Couleur - 1]

class PaquetDeCarte:
    def __init__(self):
        self.contenu = []

    """Remplit le paquet de cartes"""
    def remplir(self):
	    ??? = [ ??? for couleur in range(1, ???) for valeur in range( 1, ???)]

    """Renvoie la Carte qui se trouve a  la position donnee"""
    def getCarteAt(self, pos):
        if 0 <= pos < ??? :
            return ???
```
Exemple :

```python
>>> unPaquet = PaquetDeCarte()
>>> unPaquet.remplir()
>>> uneCarte = unPaquet.getCarteAt(20)
>>> print(uneCarte.getNom() + " de " + uneCarte.getCouleur())
  8 de coeur
```
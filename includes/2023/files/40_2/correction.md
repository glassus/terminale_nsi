```python linenums='1' hl_lines='27 31 34 35 37 39 42'
class Noeud:
    def __init__(self, valeur):
        '''Méthode constructeur pour la classe Noeud.
        Paramètre d'entrée : valeur (str)'''
        self.valeur = valeur
        self.gauche = None
        self.droit = None

    def getValeur(self):
        '''Méthode accesseur pour obtenir la valeur du noeud
        Aucun paramètre en entrée'''
        return self.valeur

    def droitExiste(self):
        '''Méthode renvoyant True si l'enfant droit existe
        Aucun paramètre en entrée'''
        return (self.droit is not None)

    def gaucheExiste(self):
        '''Méthode renvoyant True si l'enfant gauche existe
        Aucun paramètre en entrée'''
        return (self.gauche is not None)

    def inserer(self, cle):
        '''Méthode d'insertion de clé dans un arbre binaire de recherche
        Paramètre d'entrée : cle (int)'''
        if cle < self.valeur:
            # on insère à gauche
            if self.gaucheExiste():
                # on descend à gauche et on retente l'insertion de la clé
                self.gauche.inserer(cle)
            else:
                # on crée un fils gauche
                self.gauche = Noeud(cle)
        elif cle > self.valeur:
            # on insère à droite
            if self.droitExiste():
                # on descend à droite et on retente l'insertion de la clé
                self.droit.inserer(cle)
            else:
                # on crée un fils droit
                self.droit = Noeud(cle)
```
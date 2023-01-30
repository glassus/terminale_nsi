La classe ABR ci-dessous permet d'implémenter une structure d'arbre binaire de recherche.

```python linenums='1'
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
        if cle < ...:
            # on insère à gauche
            if self.gaucheExiste():
                # on descend à gauche et on retente l'insertion de la clé
                ...
            else:
                # on crée un fils gauche
                self.gauche = ...
        elif cle > ... :
            # on insère à droite
            if ... :
                # on descend à droite et on retente l'insertion de la clé
                ...
            else:
                # on crée un fils droit
                ... = Noeud(cle)

```

Compléter la fonction récursive `inserer` afin qu'elle permette d’insérer un nœud
dans l’arbre binaire de recherche proposé, à l’aide de sa clé.

Voici un exemple d'utilisation :

```python
>>> arbre = Noeud(7)
>>> for cle in (3, 9, 1, 6):
        arbre.inserer(cle)
>>> arbre.gauche.getValeur()
3
>>> arbre.droit.getValeur()
9
>>> arbre.gauche.gauche.getValeur()
1
>>> arbre.gauche.droit.getValeur()
6
```
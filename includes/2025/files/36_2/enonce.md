Un arbre binaire de recherche est soit vide, représenté en Python par la valeur None, soit
un nœud, contenant une étiquette et deux sous-arbres gauche et droit et représenté par
une instance de la classe Noeud donnée ci-dessous.

On considère ici que les étiquettes des nœuds sont des entiers et que les arbres binaires de
recherche considérés ne contiennent pas de doublons.

```python linenums='1'
class Noeud:
    def __init__(self, etiquette):
        '''Méthode constructeur pour la classe Noeud.
        Crée une feuille d'étiquette donnée.'''
        self.etiquette = etiquette
        self.gauche = None
        self.droit = None

    def inserer(self, cle):
        '''Insère la clé dans l'arbre binaire de recherche
        en préservant sa structure.'''
        if cle < self.etiquette:
            if self.gauche != None:
                ...
            else:
                self.gauche = ... 
        else:
            ...
                ...
            else:
                ... = Noeud(cle) 

```

Compléter la méthode récursive `inserer` afin qu’elle permette d’insérer une clé dans
l’arbre binaire de recherche non vide sur lequel on l’appelle.

Voici un exemple d'utilisation :

```python
>>> arbre = Noeud(7)
>>> for cle in (3, 9, 1, 6):
        arbre.inserer(cle)
>>> arbre.gauche.etiquette
3
>>> arbre.droit.etiquette
9
>>> arbre.gauche.gauche.etiquette
1
>>> arbre.gauche.droit.etiquette
6
```
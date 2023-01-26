```python linenums='1'
class Noeud:
    ''' Classe implémentant un noeud d'arbre binaire
    disposant de 3 attributs :
    - valeur : la valeur de l'étiquette,
    - gauche : le sous-arbre gauche.
    - droit : le sous-arbre droit. '''
    def __init__(self, v, g, d):
        self.valeur = v
        self.gauche = g
        self.droite = d

class ABR:
    ''' Classe implémentant une structure
    d'arbre binaire de recherche. '''
    def __init__(self):
        '''Crée un arbre binaire de recherche vide'''
        self.racine = None

    def est_vide(self):
        '''Renvoie True si l'ABR est vide et False sinon.'''
        return self.racine is None

    def parcours(self, tab = []):
        ''' Renvoie la liste tab complétée avec tous les
        éléments de l'ABR triés par ordre croissant. '''

        if self.est_vide():
            return tab
        else:
            self.racine.gauche.parcours(tab)
            tab.append(self.racine.valeur)
            self.racine.droite.parcours(tab)
            return tab

    def insere(self, element):
        '''Insère un élément dans l'arbre binaire de recherche.'''
        if self.est_vide():
            self.racine = Noeud(element, ABR(), ABR())
        else:
            if element < self.racine.valeur:
                self.racine.gauche.insere(element)
            else :
                self.racine.droite.insere(element)

    def recherche(self, element):
        '''
        Renvoie True si element est présent dans l'arbre
        binaire et False sinon.
        '''
        if self.est_vide():
            return False
        else:
            if element < self.racine.valeur:
                return self.racine.gauche.recherche(element)
            elif element > self.racine.valeur:
                return self.racine.droite.recherche(element)
            else:
                return True
```

:warning: Cette manière de coder le parcours est maladroite car elle conduit à ceci :

```python
>>> a.parcours()
[1, 3, 7, 9, 9]
>>> a.parcours()
[1, 3, 7, 9, 9, 1, 3, 7, 9, 9]
```

Comme le paramètre optionnel ```tab``` est un élément *mutable* (de type ```list``` ), Python ne le réinitialise pas avant chaque appel de la fonction.
Vous pouvez constater les conséquences fâcheuses.

Une solution pourrait être d'écrire ceci :
```python linenums='1'
def parcours(self, tab = None):
    ''' Renvoie la liste tab complétée avec tous les
    éléments de l'ABR triés par ordre croissant. '''
    if tab is None:
        tab = []
    if self.est_vide():
        return tab
    else:
        self.racine.gauche.parcours(tab)
        tab.append(self.racine.valeur)
        self.racine.droite.parcours(tab)
        return tab
```
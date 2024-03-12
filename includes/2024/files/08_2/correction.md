```python linenums='1' hl_lines='31 33-36'
class Noeud:
    '''
    classe implémentant un noeud d'arbre binaire
    '''

    def __init__(self, g, v, d):
        '''
        un objet Noeud possède 3 attributs :
        - gauche : le sous-arbre gauche,
        - valeur : la valeur de l'étiquette,
        - droit : le sous-arbre droit.
        '''
        self.gauche = g
        self.valeur = v
        self.droit = d

    def __str__(self):
        '''
        renvoie la représentation du noeud en chaine de caractères
        '''
        return str(self.valeur)

    def est_une_feuille(self):
        '''
        renvoie True si et seulement si le noeud est une feuille
        '''
        return self.gauche is None and self.droit is None


def expression_infixe(e):
    s = ''
    if e.gauche is not None:
        s = '(' + s + expression_infixe(e.gauche)
    s = s + str(e.valeur)
    if e.droit is not None:
        s = s + expression_infixe(e.droit) + ')'
    return s
```
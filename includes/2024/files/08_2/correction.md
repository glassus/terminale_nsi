```python linenums='1' hl_lines='21 23-26'
class Expr:
    """Classe implémentant un arbre d'expression."""

    def __init__(self, g, v, d):
        """un objet Expr possède 3 attributs :
        - gauche : la sous-expression gauche ;
        - valeur : la valeur de l'étiquette, opérande ou nombre ;
        - droite : la sous-expression droite."""
        self.gauche = g
        self.valeur = v
        self.droite = d

    def est_une_feuille(self):
        """renvoie True si et seulement 
        si le noeud est une feuille"""
        return self.gauche is None and self.droite is None

    def infixe(self):
        """renvoie la représentation infixe de l'expression en
        chaine de caractères"""
        s = '' 
        if self.gauche is not None:
            s = '(' + s + self.gauche.infixe() 
        s = s + str(self.valeur) 
        if self.droite is not None: 
            s = s + self.droite.infixe() + ')' 
        return s
```
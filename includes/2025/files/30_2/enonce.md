Une expression arithmétique ne comportant que les quatre opérations +, −, ×, ÷ peut être
représentée sous forme d’arbre binaire. Les nœuds internes sont des opérateurs et les feuilles
sont des nombres. Dans un tel arbre, la disposition des nœuds joue le rôle des parenthèses que
nous connaissons bien.  

![image](data2023/21_arbre.png){: .center width=30%}

En parcourant en profondeur infixe l’arbre binaire ci-dessus, on
retrouve l’expression notée habituellement :  


$$(3 \times (8 + 7)) − (2 + 1)$$


La classe `Expr` ci-après permet d’implémenter une structure
d’arbre binaire pour représenter de telles expressions.

Compléter la méthode récursive `infixe` qui renvoie une chaîne de caractères contenant
des parenthèses représentant l’expression arithmétique sur laquelle on l’applique.


```python linenums='1'
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
        s = ... 
        if self.gauche is not None:
            s = '(' + s + ... .infixe() 
        s = s + ... 
        if ... is not None: 
            s = s + ... + ... 
        return s

```

Exemples :

```python
>>> a = Expr(Expr(None, 1, None), '+', Expr(None, 2, None))
>>> a.infixe()
'(1+2)'
>>> b = Expr(Expr(Expr(None, 1, None), '+', Expr(None, 2, None)), '*', Expr(Expr(None, 3, None), '+', Expr(None, 4, None)))
>>> b.infixe()
'((1+2)*(3+4))'
>>> e = Expr(Expr(Expr(None, 3, None), '*', Expr(Expr(None, 8, None), '+', Expr(None, 7, None))),
'-', Expr(Expr(None, 2, None), '+', Expr(None, 1, None)))
>>> e.infixe()
'((3*(8+7))-(2+1))'
```
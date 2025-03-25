Un arbre binaire est soit vide, représenté en Python par la valeur `None`, soit un nœud,
contenant une étiquette et deux sous-arbres gauche et droit et représenté par une instance
de la classe `Noeud` donnée ci-dessous.


```python
class Noeud:
    def __init__(self, etiquette, gauche, droit):
        self.v = etiquette
        self.gauche = gauche
        self.droit = droit
```

![image](data2023/29_arbre1.png){: .center}

L’arbre ci-dessus sera donc implémenté de la manière suivante :
```python
a = Noeud(1, Noeud(4, None, None), Noeud(0, None, Noeud(7, None, None)))
```

Écrire une fonction récursive `taille` prenant en paramètre un arbre `a` et qui renvoie la
taille de l’arbre que cette instance implémente.

Écrire de même une fonction récursive `hauteur` prenant en paramètre un arbre `a` et qui
renvoie la hauteur de l’arbre que cette instance implémente.

On considère que la hauteur d’un arbre vide est -1 et la taille d’un arbre vide est 0.



Exemples :

```python
>>> hauteur(a)
2
>>> taille(a)
4
>>> hauteur(None)
-1
>>> taille(None)
0
>>> hauteur(Noeud(1, None, None))
0
>>> taille(Noeud(1, None, None))
1
```
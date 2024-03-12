Un arbre binaire est implémenté par la classe `Arbre` donnée ci-dessous.
Les attributs `fg` et `fd` prennent pour valeurs des instances de la classe `Arbre` ou `None`.

```python
class Arbre:
    def __init__(self, etiquette):
        self.v = etiquette
        self.fg = None
        self.fd = None
```

![image](data2023/29_arbre1.png){: .center}

L’arbre ci-dessus sera donc implémenté de la manière suivante :
```python
a = Arbre(1)
a.fg = Arbre(4)
a.fd = Arbre(0)
a.fd.fd = Arbre(7)
```



Écrire une fonction récursive `taille` prenant en paramètre une instance `a` de la classe
`Arbre` et qui renvoie la taille de l’arbre que cette instance implémente.

Écrire de même une fonction récursive `hauteur` prenant en paramètre une instance `a`
de la classe `Arbre` et qui renvoie la hauteur de l’arbre que cette instance implémente.

Si un arbre a un seul nœud, sa taille et sa hauteur sont égales à 1.
S’il est vide, sa taille et sa hauteur sont égales à 0.

Tester les deux fonctions sur l’arbre représenté ci-dessous :

![image](data2023/29_arbre2.png){: .center}


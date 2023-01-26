Dans cet exercice, les nombres sont des entiers ou des flottants.


Écrire une fonction `moyenne` renvoyant la moyenne pondérée d’une liste non vide,
passée en paramètre, de tuples à deux éléments de la forme (`valeur`,
`coefficient`) où `valeur` et `coefficient` sont des nombres positifs ou nuls.
Si la somme des coefficients est nulle, la fonction renvoie `None`, si la somme des
coefficients est non nulle, la fonction renvoie, sous forme de flottant, la moyenne des
valeurs affectées de leur coefficient.

Exemple :
```python
>>> moyenne([(8, 2), (12, 0), (13.5, 1), (5, 0.5)])
9.142857142857142
>>> moyenne([(3, 0), (5, 0)])
None
```

Dans le premier exemple la moyenne est calculée par la formule :

$\dfrac{8 \times 2 + 12 \times 0 + 13,5 \times 1 + 5 \times 0,5}{2+0+1+0,5}$
Écrire en langage Python une fonction `recherche` prenant comme paramètres une
variable `a` de type numérique (`float` ou `int`) et un tableau `tab` (type `list`) et qui
renvoie le nombre d'occurrences de `a` dans `tab`.

Exemples :
```python
>>> recherche(5, [])
0
>>> recherche(5, [-2, 3, 4, 8])
0
>>> recherche(5, [-2, 3, 1, 5, 3, 7, 4])
1
>>> recherche(5, [-2, 5, 3, 5, 4, 5])
3
```
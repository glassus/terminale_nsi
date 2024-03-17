Écrire une fonction `compte_occurrences` prenant en paramètres une valeur `x` et un
tableau `tab` (de type `list`) et renvoyant le nombre d’occurrences de `x` dans `tab`.

L’objectif de cet exercice étant de parcourir un tableau, il est interdit d’utiliser la méthode
`count` des listes Python.


Exemples :

```python
>>> compte_occurrences(5, [])
0
>>> compte_occurrences(5, [-2, 3, 1, 5, 3, 7, 4])
1
>>> compte_occurrences('a', ['a','b','c','a','d','e','a'])
3
```
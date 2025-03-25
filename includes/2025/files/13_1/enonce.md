Écrire une fonction `recherche` qui prend en paramètres `elt` un nombre entier et `tab`
un tableau de nombres entiers (type `list`), et qui renvoie l’indice de la première occurrence de `elt` dans `tab` si `elt` est dans `tab` et `None` sinon.

L’objectif de cet exercice est de parcourir un tableau, il est interdit d’utiliser la méthode
`index` des listes Python.

Exemples :
```python
>>> recherche(1, [2, 3, 4]) # renvoie None
>>> recherche(1, [10, 12, 1, 56])
2
>>> recherche(50, [1, 50, 1])
1
>>> recherche(15, [8, 9, 10, 15])
3
```
Écrire une fonction `recherche` qui prend en paramètres `elt` un nombre entier et `tab`
un tableau de nombres entiers, et qui renvoie l’indice de la première occurrence de `elt`
dans `tab` si `elt` est dans `tab` et `-1` sinon.

Ne pas oublier d’ajouter au corps de la fonction une documentation et une ou plusieurs
assertions pour vérifier les pré-conditions.

Exemples :
```python
>>> recherche(1, [2, 3, 4])
-1
>>> recherche(1, [10, 12, 1, 56])
2
>>> recherche(50, [1, 50, 1])
1
>>> recherche(15, [8, 9, 10, 15])
3
```
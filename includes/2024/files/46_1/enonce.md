Écrire une fonction `recherche` qui prend en paramètres un tableau `tab` de nombres
entiers triés par ordre croissant et un nombre entier `n`, et qui effectue une recherche
dichotomique du nombre entier `n` dans le tableau non vide `tab`.

Cette fonction doit renvoyer un indice correspondant au nombre cherché s’il est dans le
tableau, `-1` sinon.

Exemples :
```python
>>> recherche([2, 3, 4, 5, 6], 5)
3
>>> recherche([2, 3, 4, 6, 7], 5)
-1
```
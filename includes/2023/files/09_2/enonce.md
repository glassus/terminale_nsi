Soit `tab` un tableau non vide d'entiers triés dans l'ordre croissant et `n` un entier.

La fonction `chercher` ci-dessous doit renvoyer un indice où la valeur `n`
apparaît dans `tab` si cette valeur y figure et `None` sinon. 

Les paramètres de la fonction sont :

- `tab`, le tableau dans lequel s'effectue la recherche ;
- `n`, l'entier à chercher dans le tableau ;
- `i`, l'indice de début de la partie du tableau où s'effectue la recherche ;
- `j`, l'indice de fin de la partie du tableau où s'effectue la recherche.

L’algorithme demandé est une recherche dichotomique récursive.

Recopier et compléter le code de la fonction `chercher` suivante :

```python linenums='1'
def chercher(tab, n, i, j):
    if i < 0 or j > len(tab) :
        return None
    if i > j :
        return None
    m = (i + j) // ...
    if ... < n :
        return chercher(tab, n, ... , ...)
    elif ... > n :
        return chercher(tab, n, ... , ... )
    else :
        return ...
```

L'exécution du code doit donner :
```python
>>> chercher([1, 5, 6, 6, 9, 12], 7, 0, 10)

>>> chercher([1, 5, 6, 6, 9, 12], 7, 0, 5)

>>> chercher([1, 5, 6, 6, 9, 12], 9, 0, 5)
4
>>> chercher([1, 5, 6, 6, 9, 12], 6, 0, 5)
2
```
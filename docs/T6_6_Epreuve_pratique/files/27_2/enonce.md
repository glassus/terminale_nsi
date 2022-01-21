On considère l'algorithme de tri de tableau suivant : à chaque étape, on parcourt depuis
le début du tableau tous les éléments non rangés et on place en dernière position le plus
grand élément.

Exemple avec le tableau : ```t = [41, 55, 21, 18, 12, 6, 25]``` 

- Étape 1 : on parcourt tous les éléments du tableau, on permute le plus grand élément avec le dernier.

Le tableau devient `t = [41, 25, 21, 18, 12, 6, 55]`

- Étape 2 : on parcourt tous les éléments **sauf le dernier**, on permute le plus grand élément trouvé avec l'avant dernier.

Le tableau devient : ```t = [6, 25, 21, 18, 12, 41, 55]``` 

Et ainsi de suite. La code de la fonction `tri_iteratif` qui implémente cet algorithme est donné ci-
dessous.

```python linenums='1'
def tri_iteratif(tab):
    for k in range(..., 0 ,-1):
        imax = ...
        for i in range(0, ...):
            if tab[i] > ... :
                imax = i
        if tab[max] > ... :
            ..., tab[imax] = tab[imax], ...
    return tab
```

Compléter le code qui doit donner :

```python
>>> tri_iteratif([41, 55, 21, 18, 12, 6, 25])
[6, 12, 18, 21, 25, 41, 55]
``` 

On rappelle que l'instruction ```a, b = b, a``` échange les contenus de ```a``` et ```b```.

On considère l'algorithme de tri de tableau suivant : à chaque étape, on parcourt le sous-
tableau des éléments non rangés et on place le plus petit élément en première position de
ce sous-tableau.

Exemple avec le tableau : ```t = [41, 55, 21, 18, 12, 6, 25]``` 

- Étape 1 : on parcourt tous les éléments du tableau, on permute le plus petit élément avec
le premier. Le tableau devient `t = [6, 55, 21, 18, 12, 41, 25]`

- Étape 2 : on parcourt tous les éléments sauf le premier, on permute le plus petit élément
trouvé avec le second. Le tableau devient : ```t = [6, 12, 21, 18, 55, 41, 25]``` 

Et ainsi de suite. 

La code de la fonction `tri_selection` qui implémente cet algorithme est donné ci-
dessous.


```python linenums='1'
def tri_selection(tab):
    N = len(tab)
    for k in range(...):
        imin = ...
        for i in range(... , N):
            if tab[i] < ... :
                imin = i
        ... , tab[imin] = tab[imin] , ...
```

Compléter le code de cette fonction de façon à obtenir :

```python
>>> liste = [41, 55, 21, 18, 12, 6, 25]
>>> tri_selection(liste)
>>> liste
[6, 12, 18, 21, 25, 41, 55]
``` 

On rappelle que l'instruction ```a, b = b, a``` échange les contenus de ```a``` et de ```b```.

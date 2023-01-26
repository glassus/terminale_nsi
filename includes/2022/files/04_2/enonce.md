Soit une image binaire représentée dans un tableau à 2 dimensions. Les éléments
`M[i][j]`, appelés pixels, sont égaux soit à `0` soit à `1`.

Une composante d’une image est un sous-ensemble de l’image constitué uniquement de
`1` et de `0` qui sont côte à côte, soit horizontalement soit verticalement.

Par exemple, les composantes de
![image](data/252a.png){: .center width=30%}
sont
![image](data/252b.png){: .center width=30%}

On souhaite, à partir d’un pixel égal à `1` dans une image `M`, donner la valeur `val` à tous
les pixels de la composante à laquelle appartient ce pixel.

La fonction `propager` prend pour paramètre une image `M`, deux entiers `i` et `j` et une
valeur entière `val`. Elle met à la valeur `val` tous les pixels de la composante du pixel
`M[i][j]` s’il vaut `1` et ne fait rien s’il vaut `0`.

Par exemple, `propager(M,2,1,3)` donne
![image](data/252c.png){: .center width=30%}

Compléter le code récursif de la fonction `propager` donné ci-dessous :

```python linenums='1'
def propager(M, i, j, val):
    if M[i][j]== ...:
        return None # (1)

    M[i][j] = val

    # l'élément en haut fait partie de la composante
    if ((i-1) >= 0 and M[i-1][j] == ...):
        propager(M, i-1, j, val)

    # l'élément en bas fait partie de la composante
    if ((...) < len(M) and M[i+1][j] == 1):
        propager(M, ..., j, val)

    # l'élément à gauche fait partie de la composante
    if ((...) >= 0 and M[i][j-1] == 1):
        propager(M, i, ..., val)

    # l'élément à droite fait partie de la composante
    if ((...) < len(M) and M[i][j+1] == 1): # (2)
        propager(M, i, ..., val)
```

1. Dans l'énoncé original, il n'y a rien après le ```return```. 
2. Il faudrait écrire ```len(M[0])``` plutôt que  ```len(M)```. (équivalent ici car l'image est carrée...)

Exemple :
```python
>>> M = [[0,0,1,0],[0,1,0,1],[1,1,1,0],[0,1,1,0]]
>>> propager(M,2,1,3)
>>> M
[[0, 0, 1, 0], [0, 3, 0, 1], [3, 3, 3, 0], [0, 3, 3, 0]]
```
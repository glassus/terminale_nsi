Soit une image binaire représentée dans un tableau à 2 dimensions. Les éléments
`M[i][j]`, appelés pixels, sont égaux soit à `0` soit à `1`.

Une composante d’une image est un sous-ensemble de l’image constitué uniquement de
`1` et de `0` qui sont côte à côte, soit horizontalement soit verticalement.

Par exemple, les composantes de
![image](data2023/36_carre1.png){: .center}
sont
![image](data2023/36_carre2.png){: .center width=30%}

On souhaite, à partir d’un pixel égal à `1` dans une image `M`, donner la valeur `val` à tous
les pixels de la composante à laquelle appartient ce pixel.

La fonction `propager` prend pour paramètre une image `M` (représentée par une liste de
listes), deux entiers `i` et `j` et unevaleur entière `val`. Elle met à la valeur `val` tous les pixels de la composante du pixel
`M[i][j]` s’il vaut `1` et ne fait rien s’il vaut `0`.

Par exemple, `propager(M, 2, 1, 3)` donne
![image](data2023/36_carre3.png){: .center width=30%}

Compléter le code récursif de la fonction `propager` donné ci-dessous :

```python linenums='1'
def propager(M, i, j, val):
    if M[i][j] == ...:
        M[i][j] = val

    # l'element en haut fait partie de la composante
    if i-1 >= 0 and M[i-1][j] == ...:
        propager(M, i-1, j, val)

    # l'element en bas fait partie de la composante
    if ... < len(M) and M[i+1][j] == 1:
        propager(M, ..., j, val)

    # l'element à gauche fait partie de la composante
    if ... and M[i][j-1] == 1:
        propager(M, ..., ..., val)

    # l'element à droite fait partie de la composante
    if ... and ...:
        propager(..., ..., ..., ...)
```

Exemple :
```python
>>> M = [[0, 0, 1, 0], [0, 1, 0, 1], [1, 1, 1, 0], [0, 1, 1, 0]]
>>> propager(M, 2, 1, 3)
>>> M
[[0, 0, 1, 0], [0, 3, 0, 1], [3, 3, 3, 0], [0, 3, 3, 0]]
```
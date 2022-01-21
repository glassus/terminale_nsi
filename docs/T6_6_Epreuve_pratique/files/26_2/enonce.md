On considère la fonction `separe` ci-dessous qui prend en argument un tableau `tab` dont
les éléments sont des `0` et des `1` et qui sépare les `0` des `1` en plaçant les `0` en début de
tableau et les `1` à la suite.

```python linenums='1'
def separe(tab):
    i = 0
    j = ...
    while i < j :
        if tab[i] == 0 :
            i = ...
        else :
            tab[i], tab[j] = ...
            j = ...
    return tab
```

Compléter la fonction `separe` ci-dessus.

Exemples :

```python
>>> separe([1, 0, 1, 0, 1, 0, 1, 0])
[0, 0, 0, 0, 1, 1, 1, 1]
>>> separe([1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0])
[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
```
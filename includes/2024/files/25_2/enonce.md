On considère la fonction `separe` ci-dessous qui prend en argument un tableau `tab` dont
les éléments sont des `0` et des `1` et qui sépare les `0` des `1` en plaçant les `0` en début de
tableau et les `1` à la suite.

```python linenums='1'
def separe(tab):
    gauche = 0
    droite = ...
    while gauche < droite :
        if tab[gauche] == 0 :
            gauche = ...
        else :
            tab[gauche], tab[droite] = ...
            droite = ...
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

Description d’étapes effectuées par la fonction separe sur le tableau ci-dessous :
`tab = [1, 0, 1, 0, 1, 0, 1, 0]`


- **Etape 1 :** on regarde la première case, qui contient un 1 : ce 1 va aller dans la seconde
partie du tableau final et on l’échange avec la dernière case.
Il est à présent bien positionné : on ne prend plus la dernière case en compte.  
`tab = [0, 0, 1, 0, 1, 0, 1, 1]`

- **Etape 2 :** on regarde à nouveau la première case, qui contient maintenant un 0 : ce 0 va
aller dans la première partie du tableau final et est bien positionné : on ne prend plus la
première case en compte.  
`tab = [0, 0, 1, 0, 1, 0, 1, 1]`

- **Etape 3 :** on regarde la seconde case, qui contient un 0 : ce 0 va aller dans la première
partie du tableau final et est bien positionné : on ne prend plus la seconde case en compte.  
`tab = [0, 0, 1, 0, 1, 0, 1, 1]`

- **Etape 4 :** on regarde la troisième case, qui contient un 1 : ce 1 va aller dans la seconde
partie du tableau final et on l’échange avec l’avant-dernière case.
Il est à présent bien positionné : on ne prend plus l’avant-dernière case en compte.  
`tab = [0, 0, 1, 0, 1, 0, 1, 1]`

Et ainsi de suite...

`tab = [0, 0, 0, 0, 1, 1, 1, 1]`

Compléter la fonction `separe` présentée à la page précédente
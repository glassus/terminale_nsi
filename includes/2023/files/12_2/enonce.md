On dispose d’un ensemble d’objets dont on connaît, pour chacun, la masse. On
souhaite ranger l’ensemble de ces objets dans des boites identiques de telle
manière que la somme des masses des objets contenus dans une boîte ne dépasse
pas la capacité `c` de la boîte. On souhaite utiliser le moins de boîtes possibles pour
ranger cet ensemble d’objets.


Pour résoudre ce problème, on utilisera un algorithme glouton consistant à placer
chacun des objets dans la première boîte où cela est possible.

Par exemple, pour ranger dans des boîtes de capacité `c = 5` un ensemble de trois
objets dont les masses sont représentées en Python par la liste `[1, 5, 2]`, on
procède de la façon suivante :

- Le premier objet, de masse 1, va dans une première boite.
- Le deuxième objet, de masse 5, ne peut pas aller dans la même boite que le
premier objet car cela dépasserait la capacité de la boite. On place donc cet
objet dans une deuxième boîte.
- Le troisième objet, de masse 2, va dans la première boîte.

On a donc utilisé deux boîtes de capacité `c = 5` pour ranger les 3 objets.

Compléter la fonction Python `empaqueter(liste_masses, c)` suivante pour
qu’elle renvoie le nombre de boîtes de capacité c nécessaires pour empaqueter un
ensemble d’objets dont les masses sont contenues dans la liste `liste_masses`.

```python linenums='1'
def empaqueter(liste_masses, c):
    n = len(liste_masses)
    nb_boites = 0
    boites = [0]*n
    for masse in ... :
        i = 0
        while i <= nb_boites and boites[i] + ... > C:
            i = i + 1
        if i == nb_boites + 1:
            ...
        boites[i] = ...
    return ...
```

Tester ensuite votre fonction :
```python
>>> empaqueter([7, 6, 3, 4, 8, 5, 9, 2], 11)
5
```

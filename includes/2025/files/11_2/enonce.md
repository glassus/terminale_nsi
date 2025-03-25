On considère un tableau non vide de nombre entiers, positifs ou négatifs, et on souhaite déterminer
la plus grande somme possible de ses éléments consécutifs.


Par exemple, dans le tableau `[1, -2, 3, 10, -4, 7, 2, -5]`, la plus grande
somme est 18 obtenue en additionnant les éléments 3, 10, -4, 7, 2.


Pour cela, on va résoudre le problème par programmation dynamique. Si on note `tab` le
tableau considéré et `i` un indice dans ce tableau, on se ramène à un problème plus simple : déterminer la plus grande somme possible de ses éléments consécutifs se terminant à
l’indice `i`.


Si on connait la plus grande somme possible de ses éléments consécutifs se terminant à
l’indice `i-1`, on peut déterminer la plus grande somme possible de ses éléments consécutifs
se terminant à l’indice `i` :

- soit on obtient une plus grande somme en ajoutant `tab[i]` à cette somme précédente ;
- soit on commence une nouvelle somme à partir de `tab[i]`.

*Remarque :* les sommes considérées contiennent toujours au moins un terme.


Compléter la fonction `somme_max` ci-dessous qui réalise cet algorithme.

```python linenums='1'
def somme_max(tab):
    n = len(tab)
    sommes_max = [0]*n
    sommes_max[0] = tab[0]
    # on calcule la plus grande somme se terminant en i
    for i in range(1,n):
        if ... + ... > ...: 
            sommes_max[i] = ... 
        else:
            sommes_max[i] = ... 
    # on en déduit la plus grande somme de celles-ci
    maximum = 0
    for i in range(1, n):
        if ... > ...: 
            maximum = i

    return sommes_max[...] 
```

Exemples :

```python
>>> somme_max([1, 2, 3, 4, 5])
15
>> somme_max([1, 2, -3, 4, 5])
9
>>> somme_max([1, 2, -2, 4, 5])
10
>>> somme_max([1, -2, 3, 10, -4, 7, 2, -5])
18
```
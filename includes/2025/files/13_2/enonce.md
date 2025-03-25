On considère la fonction `insere` ci-dessous qui prend en argument un tableau `tab` d’entiers triés par ordre croissant et un entier `a`. 

Cette fonction crée et renvoie un nouveau tableau à partir de celui fourni en paramètre en y
insérant la valeur `a` de sorte que le tableau renvoyé soit encore trié par ordre croissant. Les
tableaux seront représentés sous la forme de listes Python.

```python linenums='1'
def insere(tab, a):
    """
    Insère l'élément a (int) dans le tableau tab (list)
    trié par ordre croissant à sa place et renvoie le
    nouveau tableau.
    """
    tab_a = [ a ] + tab # nouveau tableau contenant a 
                        # suivi des éléments de tab
    i = 0
    while i < ... and a > ...: 
        tab_a[i] = ... 
        tab_a[i+1] = a
        i = ... 
    return tab_a

```

Compléter la fonction ```insere``` ci-dessus.

Exemples :
```python
>>> insere([1, 2, 4, 5], 3)
[1, 2, 3, 4, 5]
>>> insere([1, 2, 7, 12, 14, 25], 30)
[1, 2, 7, 12, 14, 25, 30]
>>> insere([2, 3, 4], 1)
[1, 2, 3, 4]
>>> insere([], 1)
[1]
```
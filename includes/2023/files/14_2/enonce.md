On considère la fonction `insere` ci-dessous qui prend en argument un entier `a` et un
tableau `tab` d'entiers triés par ordre croissant. Cette fonction crée et renvoie un nouveau
tableau à partir de celui fourni en paramètre en y insérant la valeur `a` de sorte que le
tableau renvoyé soit encore trié par ordre croissant. Les tableaux seront représentés sous
la forme de listes Python.


```python linenums='1'
def insere(a, tab):
    """
    Insère l'élément a (int) dans le tableau tab (list)
    trié par ordre croissant à sa place et renvoie le
    nouveau tableau.
    """
    l = list(tab) #l contient les mêmes éléments que tab
    l.append(a)
    i = ...
    while a < ... and i >= 0:
        l[i+1] = ...
        l[i] = a
        i = ...
    return l
```

Compléter la fonction ```insere``` ci-dessus.

Exemples :
```python
>>> insere(3, [1, 2, 4, 5])
[1, 2, 3, 4, 5]
>>> insere(30, [1, 2, 7, 12, 14, 25])
[1, 2, 7, 12, 14, 25, 30]
>>> insere(1, [2, 3, 4])
[1, 2, 3, 4]
>>> insere(1, [])
[1]
```
On considère la fonction `insere` ci-dessous qui prend en argument un entier `a` et un
tableau `tab` d'entiers triés par ordre croissant. Cette fonction insère la valeur `a` dans le
tableau et renvoie le nouveau tableau. Les tableaux seront représentés sous la forme de
listes python.


```python linenums='1'
def insere(a, tab):
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
>>> insere(3,[1,2,4,5])
[1, 2, 3, 4, 5]
>>> insere(10,[1,2,7,12,14,25])
[1, 2, 7, 10, 12, 14, 25]
>>> insere(1,[2,3,4])
[1, 2, 3, 4]
```
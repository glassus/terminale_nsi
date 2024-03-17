Cet exercice utilise des piles qui seront représentées par des listes Python.

Si `pile` est une pile, alors `pile == []` indique si la pile est vide, `pile.pop()` retire
et renvoie le sommet de la pile et `pile.append(v)` ajoute la valeur `v` au sommet de la
pile.

Si on considère qu’une fonction manipule une pile, elle ne peut pas utiliser d’autres opéra-
tions que celles décrites ci-dessus.

On cherche à écrire une fonction `positifs` qui prend une pile de nombres entiers en
paramètre et qui renvoie une nouvelle pile contenant les entiers positifs de la pile initiale,
dans le même ordre, quitte à modifier la pile initiale.

Pour cela, on va également écrire une fonction `renverse` qui prend une pile en paramètre
et qui renvoie une nouvelle pile contenant les mêmes éléments que la pile initiale, mais
dans l’ordre inverse. Cette fonction sera également amenée à modifier la pile passée en
paramètre.


Compléter le code Python des fonctions `renverse` et `positifs` ci-après

```python linenums='1'
def renverse(pile):
    '''renvoie une pile contenant les mêmes éléments que pile,
    mais dans l'ordre inverse.
    Cette fonction détruit pile.'''
    pile_inverse = ... 
    while pile != []:
        ... .append(...) 
    return ... 


def positifs(pile):
    '''renvoie une pile contenant les éléments positifs de pile,
    dans le même ordre. Cette fonction détruit pile.'''
    pile_positifs = ... 
    while pile != []:
        ... = pile.pop() 
        if ... >= 0: 
            ...
    return ... 




```

Exemple :
```python
>>> renverse([1, 2, 3, 4, 5])
[5, 4, 3, 2, 1]
>>> positifs([-1, 0, 5, -3, 4, -6, 10, 9, -8])
[0, 5, 4, 10, 9]
>>> positifs([-2])
[]
```
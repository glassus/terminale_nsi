On rappelle que les tableaux sont représentés par des listes en Python du type `list`.

Le but de cet exercice est d’écrire une fonction ajoute qui prend en paramètres trois
arguments `indice`, `element` et `tab` et renvoie un tableau `tab_ins` dans lequel les
éléments sont ceux du tableau `tab` avec, en plus, l’élément `element` à l’indice `indice`.

On considère que les variables `indice` et `element` sont des entiers positifs et que les
éléments de `tab` sont également des entiers.

En réalisant cette insertion, Les éléments du tableau `tab` dont les indices sont supérieurs
ou égaux à `indice` apparaissent décalés vers la droite dans le tableau `tab_ins`.

Si `indice` est égal au nombre d’éléments du tableau `tab`, l’élément `element` est ajouté
dans `tab_ins` après tous les éléments du tableau `tab`.

Exemples :

```python
>>> ajoute(1, 4, [7, 8, 9])
[7, 4, 8, 9]
>>> ajoute(3, 4, [7, 8, 9])
[7, 8, 9, 4]
>>> ajoute(0, 4, [7, 8, 9])
[4, 7, 8, 9]
```

Compléter et tester le code ci-dessous :

```python linenums='1'
def ajoute(indice, element, tab):
    '''Renvoie un nouveau tableau obtenu en insérant
    element à l'indice indice dans le tableau tab.'''
    nbre_elts = len(tab)
    tab_ins = [0] * (nbre_elts + 1)
    for i in range(indice):
        tab_ins[i] = ... 
    tab_ins[...] = ... 
    for i in range(indice + 1, nbre_elts + 1):
        tab_ins[i] = ... 
    return tab_ins

```

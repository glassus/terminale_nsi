La méthode `insert` de la classe `list` permet d’insérer un élément dans une liste à un
`indice` donné.

Le but de cet exercice est, *sans utiliser cette méthode*, d’écrire une fonction `ajoute`
réalisant cette insertion en produisant une nouvelle liste.

Cette fonction `ajoute` prend en paramètres trois variables `indice`, `element` et `liste`
et renvoie une liste `L` dans laquelle les éléments sont ceux de la liste `liste` avec, en
plus, l’élément `element` à l’indice `indice`.  
On considère que les variables `indice` et `element` sont des entiers positifs et que les
éléments de `liste` sont également des entiers positifs.  
Les éléments de la liste `liste`, dont les indices sont supérieurs ou égaux à `indice`
apparaissent décalés vers la droite dans la liste `L`.  
Si `indice` est supérieur ou égal au nombre d’éléments de la liste `liste`, l’élément
element est ajouté dans `L` après tous les éléments de la liste `liste`.

Exemple :
```python
>>> ajoute(1, 4, [7, 8, 9])
[7, 4, 8, 9]
>>> ajoute(3, 4, [7, 8, 9])
[7, 8, 9, 4]
>>> ajoute(4, 4, [7, 8, 9])
[7, 8, 9, 4]
```

Compléter et tester le code ci-dessous :

```python linenums='1'
def ajoute(indice, element, liste):
    nbre_elts = len(liste)
    L = [0 for i in range(nbre_elts + 1)]
    if ...:
        for i in range(indice):
            L[i] = ...
        L[...] = ...
        for i in range(indice + 1, nbre_elts + 1):
            L[i] = ...
    else:
        for i in range(nbre_elts):
            L[i] = ...
        L[...] = ...
    return L
```

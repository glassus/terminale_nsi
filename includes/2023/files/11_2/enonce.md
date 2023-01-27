La fonction `tri_insertion` suivante prend en argument une liste `tab` et trie cette liste en
utilisant la méthode du tri par insertion. Compléter cette fonction pour qu'elle réponde à la
spécification demandée.

On rappelle le principe du tri par insertion : on considère les éléments à trier un par un,
le premier élément constituant, à lui tout seul, une liste triée de longueur 1. On range
ensuite le second élément pour constituer une liste triée de longueur 2, puis on range le
troisième élément pour avoir une liste triée de longueur 3 et ainsi de suite… A chaque
étape, le premier élément de la sous-liste non triée est placé dans la sous-liste des
éléments déjà triés de sorte que cette sous-liste demeure triée.  

Le principe du tri par insertion est donc d'insérer à la n-ième itération, le n-ième élément
à la bonne place.


```python linenums='1'
def tri_insertion(tab):
    n = len(tab)
    for i in range(1, n):
        valeur_insertion = tab[...]
        # la variable j sert à déterminer où placer la valeur à ranger
        j = ...
        # tant qu'on a pas trouvé la place de l'élément à insérer
        # on décale les valeurs du tableau vers la droite
        while j > ... and valeur_insertion < tab[...]:
            tab[j] = tab[j-1]
            j = ...
        tab[j] = ...
```

Exemples :
```python
>>> liste = [9, 5, 8, 4, 0, 2, 7, 1, 10, 3, 6]
>>> tri_insertion(liste)
>>> liste
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```
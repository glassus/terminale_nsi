On s’intéresse à un algorithme récursif qui permet de rendre la monnaie à partir d’une
liste donnée de valeurs de pièces et de billets.

Le système monétaire est donné sous
forme d’une liste `pieces=[100, 50, 20, 10, 5, 2, 1]`.
(on supposera qu’il n’y a
pas de limitation quant à leur nombre).

On cherche à donner la liste de pièces à rendre
pour une somme donnée en argument.
Compléter le code Python ci-dessous de la fonction `rendu_glouton` qui implémente cet
algorithme et renvoie la liste des pièces à rendre.

```python linenums='1'
pieces = [100,50,20,10,5,2,1] # (1)

def rendu_glouton(arendre, solution=[], i=0):
    if arendre == 0:
        return ...
    p = pieces[i]
    if p <= ... :
        solution.append(...)
        return rendu_glouton(arendre - p, solution,i)
    else :
        return rendu_glouton(arendre, solution, ...)
```

1. Erreur dans l'énoncé officiel : ```Pieces```


On devra obtenir :

```python
>>> rendu_glouton(68, [], 0) 
[50, 10, 5, 2, 1]
>>> rendu_glouton(291, [], 0) 
[100, 100, 50, 20, 20, 1]
```

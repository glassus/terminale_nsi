On considère dans cet exercice un graphe orienté représenté sous forme de listes d’adjacence.

On suppose que les sommets sont numérotés de `0` à `n-1`.

Par exemple, le graphe suivant :

![image](data2024/graph2.png){: .center}

est représenté par la liste d’adjacence suivante :

```python
adj = [[1, 2], [2], [0], [0]]
```

Écrire une fonction `voisins_entrants(adj, x)` qui prend en paramètre le graphe
donné sous forme de liste d’adjacence et qui renvoie une liste contenant les voisins entrants
du sommet `x`, c’est-à-dire les sommets `y` tels qu’il existe une arête de `y` vers `x`.

Exemples :

```python
>>> voisins_entrants([[1, 2], [2], [0], [0]], 0)
[2, 3]
>>> voisins_entrants([[1, 2], [2], [0], [0]], 1)
[0]
```

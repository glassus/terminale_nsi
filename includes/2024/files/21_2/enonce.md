Dans cet exercice, on considère un graphe non orienté représenté sous forme de listes
d’adjacence. On suppose que les sommets sont numérotés de 0 à n-1.

Ainsi, le graphe suivant:

![image](data2024/graph1.png){: .center}


sera représenté par la liste d’adjacence suivante:

`adj = [[1, 2], [0, 3], [0], [1], [5], [4]]`

On souhaite déterminer les sommets accessibles depuis un sommet donné dans le graphe.
Pour cela, on va procéder à un parcours en profondeur du graphe.

Compléter la fonction suivante.

```python linenums='1'
def parcours(adj, x, acc):
    '''Réalise un parcours en profondeur récursif
    du graphe donné par les listes d'adjacence adj 
    depuis le sommet x en accumulant les sommets
    rencontrés dans acc'''
    if x ...: 
        acc.append(x)
        for y in ...: 
            parcours(adj, ...) 

def accessibles(adj, x):
    '''Renvoie la liste des sommets accessibles dans le
    graphe donné par les listes d'adjacence adj depuis
    le sommet x.'''
    acc = []
    parcours(adj, ...) 
    return acc

```

Exemples :

```python
>>> accessibles([[1, 2], [0], [0, 3], [1], [5], [4]], 0)
[0, 1, 2, 3]
>>> accessibles([[1, 2], [0], [0, 3], [1], [5], [4]], 4)
[4, 5]
```
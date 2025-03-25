```python linenums='1'
def voisins_entrants(adj, x):
    vois = []
    for i in range(len(adj)):
        if x in adj[i]:
            vois.append(i)
    return vois
```
On utilise un dictionnaire pour stocker au fur et à mesure les valeurs.
```python linenums='1'
def fibonnaci(n):
    d = {}
    d[1] = 1
    d[2] = 1
    for k in range(3, n+1):
        d[k] = d[k-1] + d[k-2]
    return d[n]
```
```python linenums='1'
def recherche(tab, n):
    indice_solution = None
    for i in range(len(tab)):
        if tab[i] == n:
            indice_solution = i
    return indice_solution
```
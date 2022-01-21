```python linenums='1'
def recherche(elt, tab):
    tab_indices = []
    for i in range(len(tab)):
        if tab[i] == elt:
            tab_indices.append(i)
    return tab_indices        
```
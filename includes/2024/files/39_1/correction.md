```python linenums='1'
def recherche(elt, tab):
    for i in range(len(tab)-1, -1, -1):
        if tab[i] == elt:
            return i
    return -1
```
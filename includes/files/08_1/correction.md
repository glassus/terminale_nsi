```python linenums='1'
def recherche(elt, tab):
    for i in range(len(tab)):
        if tab[i] == elt:
            return i        
    return -1         
```
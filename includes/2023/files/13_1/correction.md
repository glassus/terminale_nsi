```python linenums='1'
def recherche(a, tab):
    nb = 0
    for element in tab:
        if element == a:
            nb += 1
    return nb
```
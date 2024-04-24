```python linenums='1'
def compte_occurrences(x, tab):
    nb = 0
    for element in tab:
        if element == x:
            nb += 1
    return nb
```
```python linenums='1'
def nb_repetitions(elt, tab):
    nb = 0
    for element in tab:
        if element == elt:
            nb += 1
    return nb
``` 
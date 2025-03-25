```python linenums='1'
def moyenne(tab):
    somme = 0
    for elt in tab:
        somme += elt
    return somme / len(tab)
```
```python linenums='1'
def ajoute_dictionnaires(d1, d2):
    d = {}
    for cle in d1:
        d[cle] = d1[cle]
    for cle in d2:
        if cle in d:
            d[cle] += d2[cle]
        else:
            d[cle] = d2[cle]
    return d
```
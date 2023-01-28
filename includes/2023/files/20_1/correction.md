```python linenums='1'
def ajoute_dictionnaires(d1, d2):
for cle in d2:
    if cle in d1:
        d1[cle] += d2[cle]
    else:
        d1[cle] = d2[cle]
return d1
```
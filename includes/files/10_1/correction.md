```python linenums='1'
def occurrence_lettres(phrase):
    occ = {}
    for caractere in phrase:
        if caractere in occ:
            occ[caractere] += 1
        else:
            occ[caractere] = 1
    return occ
```
```python linenums='1'
def recherche_motif(motif, texte):
    sol = []
    i = 0
    while i <= len(texte) - len(motif):
        j = 0
        while j < len(motif) and motif[j] == texte[j+i]:
            j += 1
        if j == len(motif):
            sol.append(i)
        i += 1
    return sol
```
```python linenums='1'
def recherche_min(tab):
    indice_min = 0
    for i in range(len(tab)):
        if tab[i] < tab[indice_min]:
            indice_min = i
    return indice_min

```
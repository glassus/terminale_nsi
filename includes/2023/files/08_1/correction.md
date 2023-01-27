```python linenums='1'
def max_dico(dico):
    cle_max = ''
    val_max = 0
    for cle in dico:
        if dico[cle] > val_max:
            val_max = dico[cle]
            cle_max = cle
    return (cle_max, val_max)
```
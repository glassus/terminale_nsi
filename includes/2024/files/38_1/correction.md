```python linenums='1'
def indices_maxi(tab):
    val_max = tab[0]
    ind_max = []
    for i in range(len(tab)):
        if tab[i] > val_max:
            val_max = tab[i]
    for i in range(len(tab)):
        if tab[i] == val_max:
            ind_max.append(i)
    return (val_max, ind_max)


```
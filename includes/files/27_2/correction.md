```python linenums='1'
def tri_iteratif(tab):
    for k in range(len(tab)-1, 0, -1):
        imax = 0
        for i in range(0, k):
            if tab[i] > tab[imax] :
                imax = i
        if tab[imax] > tab[k] :
            tab[k], tab[imax] = tab[imax], tab[k] 
    return tab

```
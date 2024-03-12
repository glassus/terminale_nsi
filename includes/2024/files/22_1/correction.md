```python linenums='1'
def recherche_indices_classement(elt, tab):
    ind_inf = []
    ind_egal = []
    ind_sup = [] 
    for i in range(len(tab)):
        if tab[i] < elt:
            ind_inf.append(i)
        elif tab[i] > elt:
            ind_sup.append(i)
        else:
            ind_egal.append(i)
    return (ind_inf, ind_egal, ind_sup)
```
```python linenums='1'
def recherche(tab, n):
    ind_debut = 0
    ind_fin = len(tab) - 1
    while ind_debut <= ind_fin:
        ind_milieu = (ind_debut + ind_fin) // 2
        if tab[ind_milieu] == n:
            return ind_milieu
        elif tab[ind_milieu] < n:
            ind_debut = ind_milieu + 1
        else:
            ind_fin = ind_milieu - 1
    return -1


```
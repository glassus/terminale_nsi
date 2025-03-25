```python linenums='1' hl_lines='7 8 10'
def ajoute(indice, element, tab):
    '''Renvoie un nouveau tableau obtenu en insérant
    element à l'indice indice dans le tableau tab.'''
    nbre_elts = len(tab)
    tab_ins = [0] * (nbre_elts + 1)
    for i in range(indice):
        tab_ins[i] = tab[i] 
    tab_ins[indice] = element 
    for i in range(indice + 1, nbre_elts + 1):
        tab_ins[i] = tab[i-1] 
    return tab_ins

```
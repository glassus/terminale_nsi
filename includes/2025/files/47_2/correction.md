```python linenums='1' hl_lines='3 4 5 11-16'
def echange(tab, i, j):
    '''Echange les éléments d'indice i et j dans le tableau tab.'''
    temp = tab[i] 
    tab[i] = tab[j] 
    tab[j] = temp 

def tri_selection(tab):
    '''Trie le tableau tab dans l'ordre croissant
    par la méthode du tri par sélection.'''
    N = len(tab)
    for k in range(N): 
        imin = k 
        for i in range(k + 1, N): 
            if tab[i] < tab[imin]: 
                imin = i
        echange(tab, k, imin) 


```
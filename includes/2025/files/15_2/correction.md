```python linenums='1' hl_lines='7 8 9 11 13'
def chercher(tab, x, i, j):
    '''Renvoie l'indice de x dans tab, si x est dans tab, 
    None sinon.
    On suppose que tab est trié dans l'ordre croissant.'''
    if i > j:
        return None
    m = (i + j) // 2 
    if tab[m] < x: 
        return chercher(tab, x, m+1 , j) 
    elif tab[m] > x:
        return chercher(tab, x, i , m-1) 
    else:
        return m 


```
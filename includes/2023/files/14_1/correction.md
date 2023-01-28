```python linenums='1'
def recherche(elt, tab):
    '''
    renvoie l’indice de la première occurrence de
    elt dans tab si elt est dans tab et -1 sinon. 
    '''
    assert tab != [], "le tableau est vide"
    for i in range(len(tab)):
        if tab[i] == elt:
            return i        
    return -1         
```
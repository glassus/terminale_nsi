```python linenums='1'
def max_et_indice(tab):
    '''
    renvoie la valeur du plus grand élément de cette liste ainsi
    que l’indice de sa première apparition dans cette liste.
    '''
    assert tab != [], 'le tableau est vide'

    val_max = tab[0]
    ind_max = 0
    for i in range(len(tab)):
        if tab[i] > val_max:
            val_max = tab[i]
            ind_max = i
    return (val_max, ind_max)

```
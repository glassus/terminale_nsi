```python linenums='1'
def max_et_indice(tab):
    '''
    renvoie la valeur du plus grand élément de ce tableau ainsi
    que l’indice de sa première apparition dans ce tableau.
    '''
    val_max = tab[0]
    ind_max = 0
    for i in range(len(tab)):
        if tab[i] > val_max:
            val_max = tab[i]
            ind_max = i
    return (val_max, ind_max)

```
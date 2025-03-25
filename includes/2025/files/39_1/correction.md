```python linenums='1'
def moyenne(tab):
    if tab == []:
        print('Le tableau donné est vide')
        return None
    else:
        somme = 0
        for elt in tab:
            somme += elt
        return somme / len(tab)

```
```python linenums='1'
def rechercheMinMax(tab):
    if tab == []:
        return {'min': None, 'max': None}
    d = {}
    d['min'] = tab[0]
    d['max'] = tab[0]
    for val in tab:
        if val < d['min']:
            d['min'] = val
        if val > d['max']:
            d['max'] = val
    return d

```
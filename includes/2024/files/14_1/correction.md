```python linenums='1'
def min_et_max(tab):
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
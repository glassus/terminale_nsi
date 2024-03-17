```python linenums='1'
def enumere(tab):
    d = {}
    for i in range(len(tab)):
        if tab[i] in d:
            d[tab[i]].append(i)
        else:
            d[tab[i]] = [i]
    return d
```
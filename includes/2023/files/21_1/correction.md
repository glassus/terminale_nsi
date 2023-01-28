```python linenums='1'
def delta(tab):
    diff = [tab[0]]
    for i in range(1, len(tab)):
        diff.append(tab[i] - tab[i-1])
    return diff
```
```python linenums='1'
def insertion_abr(a, cle): 
    if a is None:
        return (None, cle, None)
    elif cle > a[1]:
        return (a[0], a[1], insertion_abr(a[2], cle))
    elif cle < a[1]:
        return (insertion_abr(a[0], cle), a[1], a[2])
    return a
```
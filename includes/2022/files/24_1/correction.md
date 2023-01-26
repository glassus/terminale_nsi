```python linenums='1'
def maxliste(tab):
    maximum = tab[0]
    for element in tab:
        if element > maximum:
            maximum = element
    return maximum

```
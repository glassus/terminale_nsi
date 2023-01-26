```python linenums='1'
def verifie(tab):
    for i in range(1, len(tab)):
        if tab[i] < tab[i-1]:
            return False
    return True

```
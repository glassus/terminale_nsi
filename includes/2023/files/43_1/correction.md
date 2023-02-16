```python linenums='1'
def ecriture_binaire_entier_positif(n):
    # cas particulier pour n = 0
    if n == 0:
        return [0]
    # cas général
    b = []
    while n != 0:
        b.append(n % 2)
        n = n // 2
    b.reverse()
    return b
```
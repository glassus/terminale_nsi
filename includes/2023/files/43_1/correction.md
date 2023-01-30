```python linenums='1'
def ecriture_binaire_entier_positif(n):
    # cas particulier pour n = 0
    if n == 0:
        return [0]
    # cas général
    b = []
    bits = 0
    while n != 0:
        b.append(n % 2)
        bits += 1
        n = n // 2
    b.reverse()
    return b
```
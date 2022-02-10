```python linenums='1'
def calcul(k):
    valeurs = []
    n = k
    valeurs.append(n)
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n + 1
        valeurs.append(n)
    return valeurs
```
```python linenums='1'
def multiplication(n1, n2):
    # on se ramène d'abord au cas où n1 et n2 sont tous les deux positifs :
    if n1 < 0:
        return -multiplication(-n1, n2)
    if n2 < 0:
        return -multiplication(n1, -n2)

    resultat = 0
    for _ in range(n2):
        resultat += n1
    return resultat
```
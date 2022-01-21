```python linenums='1'
def recherche(caractere, mot):
    somme = 0
    for lettre in mot:
        if lettre == caractere:
            somme += 1
    return somme
```
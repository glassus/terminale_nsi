```python linenums='1'
def recherche(caractere, chaine):
    somme = 0
    for lettre in chaine:
        if lettre == caractere:
            somme += 1
    return somme
```
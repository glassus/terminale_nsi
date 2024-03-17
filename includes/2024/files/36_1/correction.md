```python linenums='1'
def occurrences(caractere, chaine):
    somme = 0
    for lettre in chaine:
        if lettre == caractere:
            somme += 1
    return somme
```
```python linenums='1'
def moyenne(tab):
    somme = 0
    coeffs = 0
    for couple in tab:
        somme += couple[0] * couple[1]
        coeffs += couple[1]
    if coeffs == 0:
        return None
    return somme / coeffs

```
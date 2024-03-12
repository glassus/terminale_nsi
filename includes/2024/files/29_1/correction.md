```python linenums='1'
def moyenne(liste_notes):
    somme_notes = 0
    somme_coeffs = 0
    for devoir in liste_notes:
        note = devoir[0]
        coeff = devoir[1]
        somme_notes += note * coeff
        somme_coeffs += coeff
    return somme_notes / somme_coeffs
```
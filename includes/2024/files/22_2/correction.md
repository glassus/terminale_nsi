```python linenums='1' hl_lines='2 4-6 8-10'
def moyenne(nom, dico_result):
    if nom in dico_result:
        notes = dico_result[nom]
        total_points = 0.
        total_coefficients = 0
        for valeurs  in notes.values():
            note, coefficient = valeurs
            total_points = total_points + note * coefficient
            total_coefficients = total_coefficients + coefficient
        return round( total_points / total_coefficients, 1 )
    else:
        return -1
```
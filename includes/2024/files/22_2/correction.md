```python linenums='1' hl_lines='5 7 9 10 11 13 14 15'
def moyenne(nom, resultats):
    '''Renvoie la moyenne de l'élève nom, selon le dictionnaire 
    resultats. Si nom n'est pas dans le dictionnaire, 
    la fonction renvoie None.'''
    if nom in resultats: 
        notes = resultats[nom]
        if notes == {}: # pas de notes 
            return 0
        total_points = 0 
        total_coefficients = 0 
        for valeurs in notes.values(): 
            note, coefficient = valeurs
            total_points = total_points + note * coefficient 
            total_coefficients = total_coefficients + coefficient 
        return round( total_points / total_coefficients, 1 ) 
    else:
        return None
```
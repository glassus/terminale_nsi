Un professeur de NSI décide de gérer les résultats de sa classe sous la forme d’un
dictionnaire :

- les clefs sont les noms des élèves ;
- les valeurs sont des dictionnaires dont les clefs sont les types d’épreuves sous
forme de chaîne de caractères et les valeurs sont les notes obtenues associées à
leurs coefficients dans une liste.

Avec :

```python
resultats = {'Dupont': {
                        'DS1': [15.5, 4],
                        'DM1': [14.5, 1],
                        'DS2': [13, 4],
                        'PROJET1': [16, 3],
                        'DS3': [14, 4]
                    },
            'Durand': {
                        'DS1': [6 , 4],
                        'DM1': [14.5, 1],
                        'DS2': [8, 4],
                        'PROJET1': [9, 3],
                        'IE1': [7, 2],
                        'DS3': [8, 4],
                        'DS4':[15, 4]
                    }
            }
```

L’élève dont le nom est Durand a ainsi obtenu au DS2 la note de 8 avec un coefficient 4.

Le professeur crée une fonction `moyenne` qui prend en paramètre le nom d’un de ses
élèves et renvoie sa moyenne arrondie au dixième.

Compléter le code du professeur ci-dessous :

```python linenums='1'
def moyenne(nom, dico_result):
    if nom in ...:
        notes = dico_result[nom]
        total_points = ...
        total_coefficients = ...
        for ...  in notes.values():
            note, coefficient = valeurs
            total_points = total_points + ... * coefficient
            total_coefficients = ... + coefficient
        return round( ... / total_coefficients, 1 )
    else:
        return -1
```

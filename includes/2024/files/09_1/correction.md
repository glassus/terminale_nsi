```python linenums='1'
def effectif_notes(notes_eval):
    tab = [0]*11
    for note in notes_eval:
        tab[note] += 1
    return tab

def notes_triees(eff):
    triees = []
    for i in range(11):
        if eff[i] != 0: #(1)
            for _ in range(eff[i]):
                triees.append(i)
    return triees
```

1. On peut ne pas effectuer ce test, car si ```eff[i]``` vaut 0, on ne rentrera pas dans la boucle ```for _ in range(0)``` et donc on ne touchera pas à la liste ```triees```.  
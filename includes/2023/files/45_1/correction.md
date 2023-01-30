```python linenums='1'
def rangement_valeurs(notes_eval):
    lst = [0]*11
    for note in notes_eval:
        lst[note] += 1
    return lst

def notes_triees(effectifs_notes):
    triees = []
    for i in range(11):
        if effectifs_notes[i] != 0:
            for _ in range(effectifs_notes[i]):
                triees.append(i)
    return triees

```
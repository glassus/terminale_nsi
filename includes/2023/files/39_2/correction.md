```python linenums='1' hl_lines='3 5-7 9 10'
def pantheon(eleves, notes):
    note_maxi = 0
    meilleurs_eleves =  []

    for i in range(len(eleves)) :
        if notes[i] == note_maxi :
            meilleurs_eleves.append(eleves[i])
        elif notes[i] > note_maxi:
            note_maxi = notes[i]
            meilleurs_eleves = [i]

    return (note_maxi, meilleurs_eleves)
```
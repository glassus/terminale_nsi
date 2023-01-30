On considère la fonction `pantheon` prenant en paramètres `eleves` et `notes` deux
tableaux de même longueur, le premier contenant le nom des élèves et le second, des
entiers positifs désignant leur note à un contrôle de sorte que `eleves[i]` a obtenu la
note `notes[i]`.  
Cette fonction renvoie le couple constitué de la note maximale attribuée et des noms
des élèves ayant obtenu cette note regroupés dans un tableau.  
Ainsi, l’instruction `pantheon(['a', 'b', 'c', 'd'], [15, 18, 12, 18])` renvoie
le couple `(18, ['b', 'd'])`.

```python linenums='1'
def pantheon(eleves, notes):
    note_maxi = 0
    meilleurs_eleves =  ...

    for i in range(...) :
        if notes[i] == ... :
            meilleurs_eleves.append(...)
        elif notes[i] > note_maxi:
            note_maxi = ...
            meilleurs_eleves = [...]

    return (note_maxi,meilleurs_eleves)
```

Compléter ce code.

Exemples :

```python
>>> eleves_nsi = ['a','b','c','d','e','f','g','h','i','j']
>>> notes_nsi = [30, 40, 80, 60, 58, 80, 75, 80, 60, 24]
>>> pantheon(eleves_nsi, notes_nsi)
(80, ['c', 'f', 'h'])
>>> pantheon([],[])
(0, [])
```
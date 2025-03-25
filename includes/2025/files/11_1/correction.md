```python linenums='1'
def parcours_largeur(arbre):
    parcours = []
    file = [arbre]
    while file != []:
        a = file.pop(0)
        parcours.append(a[1])
        if a[0] != None:
            file.append(a[0])
        if a[2] != None:
            file.append(a[2])
    return parcours
```
```python linenums='1' hl_lines='3 6 8 9'
def separe(tab):
    gauche = 0
    droite = len(tab) - 1
    while gauche < droite :
        if tab[gauche] == 0 :
            gauche = gauche + 1
        else :
            tab[gauche], tab[droite] = tab[droite], tab[gauche]
            droite = droite - 1
    return tab
```
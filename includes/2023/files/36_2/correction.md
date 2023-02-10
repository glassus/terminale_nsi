```python linenums='1' hl_lines='2 6 10 11 14 15 18 19'
def propager(M, i, j, val):
    if M[i][j] == 1:
        M[i][j] = val

    # l'element en haut fait partie de la composante
    if i-1 >= 0 and M[i-1][j] == 1:
        propager(M, i-1, j, val)

    # l'element en bas fait partie de la composante
    if i+1 < len(M) and M[i+1][j] == 1:
        propager(M, i+1, j, val)

    # l'element à gauche fait partie de la composante
    if j-1 >= 0 and M[i][j-1] == 1:
        propager(M, i, j-1, val)

    # l'element à droite fait partie de la composante
    if j+1 < len(M[i]) and M[i][j+1] == 1:
        propager(M, i, j+1, val)

```
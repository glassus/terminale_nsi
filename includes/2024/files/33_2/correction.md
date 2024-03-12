```python linenums='1' hl_lines='8-12'
def crible(n):
    """
    Renvoie un tableau contenant tous les nombres premiers plus petits que N
    """
    premiers = []
    tab = [True] * n
    tab[0], tab[1] = False, False
    for i in range(2, n):
        if tab[i] == True:
            premiers.append(i)
            for multiple in range(2*i, n, i):
                tab[multiple] = False
    return premiers

assert crible(40) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]


```
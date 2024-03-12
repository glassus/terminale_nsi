def crible(n):
    """
    Renvoie un tableau contenant tous les nombres premiers plus petits
    que n
    """
    premiers = []
    tab = [True] * n
    tab[0], tab[1] = False, False
    for i in range(..., n):
        if tab[i] == ...:
            premiers.append(...)
            for multiple in range(2 * i, n, ...):
                tab[multiple] = ...
    return premiers


assert crible(40) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

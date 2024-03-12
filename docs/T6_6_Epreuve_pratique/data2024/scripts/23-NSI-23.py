tab_a = [3, 3, 3, 9, 9, 9, 1, 1, 1, 7, 2, 2, 2, 4, 4, 4, 8, 8, 8, 5, 5, 5]

tab_b = [8, 5, 5, 5, 9, 9, 9, 18, 18, 18, 3, 3, 3]

tab_c = [5, 5, 5, 1, 1, 1, 0, 0, 0, 6, 6, 6, 3, 8, 8, 8]

def trouver_intrus(tab, g, d):
    '''
    Renvoie la valeur de l'intrus situe entre les indices g et d
    dans la liste tab ou :
        tab verifie les conditions de l'exercice,
        g et d sont des multiples de 3.
    '''
    if g == d:
        return ...

    else:
        nombre_de_triplets = (d - g)// ...
        indice = g + 3 * (nombre_de_triplets // 2)
        if ... :
            return ...
        else:
            return ...

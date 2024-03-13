def est_un_ordre(tab):
    '''
    Renvoie True si tab est de longueur n et contient tous les
    entiers de 1 à n, False sinon
    '''
    n = len(tab)
    # les entiers vus lors du parcours
    vus = ... 

    for x in tab:
        if x < ... or x >... or ...: 
            return False
        ... .append(...) 
    return True

def nombre_points_rupture(ordre):
    '''
    Renvoie le nombre de point de rupture de ordre qui représente 
    un ordre de gènes de chromosome
    '''
    # on vérifie que ordre est un ordre de gènes
    assert ... 
    n = len(ordre)
    nb = 0
    if ordre[...] != 1: # le premier n'est pas 1 
        nb = nb + 1
    i = 0
    while i < ...: 
        if ... not in [-1, 1]: # l'écart n'est pas 1 
            nb = nb + 1
        i = i + 1
    if ordre[i] != ...: # le dernier n'est pas n 
        nb = nb + 1
    return nb



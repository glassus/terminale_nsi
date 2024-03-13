def fusion(tab1,tab2):
    '''Fusionne deux tableaux triés et renvoie
    le nouveau tableau trié.'''
    n1 = len(tab1)
    n2 = len(tab2)
    tab12 = [0] * (n1 + n2)
    i1 = 0
    i2 = 0
    i = 0
    while i1 < n1 and ...: 
        if tab1[i1] < tab2[i2]:
            tab12[i] = ... 
            i1 = ... 
        else:
            tab12[i] = tab2[i2]
            i2 = ... 
        i += 1
    while i1 < n1:
        tab12[i] = ... 
        i1 = i1 + 1
        i = ... 
    while i2 < n2:
        tab12[i] = ... 
        i2 = i2 + 1
        i = ... 
    return tab12



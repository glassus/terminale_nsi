def fusion(lst1, lst2):
    n1 = len(lst1)
    n2 = len(lst2)
    lst12 = [0] * (n1 + n2)
    i1 = 0
    i2 = 0
    i = 0
    while i1 < n1 and ... :
        if lst1[i1] < lst2[i2]:
            lst12[i] = ...
            i1 = ...
        else:
            lst12[i] = lst2[i2]
            i2 = ...
        i += 1
    while i1 < n1:
        lst12[i] = ...
        i1 = i1 + 1
        i = ...
    while i2 < n2:
        lst12[i] = ...
        i2 = i2 + 1
        i = ...
    return lst12

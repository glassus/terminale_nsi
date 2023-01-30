```python linenums='1' hl_lines='6 8-10'
def tri_bulles(T):
    '''
    Renvoie le tableau T trié par ordre croissant
    '''
    n = len(T)
    for i in range(n-1,-1,-1):
        for j in range(i):
            if T[j] > T[j+1]:
                temp = T[j]
                T[j] = T[j+1]
                T[j+1] = temp
    return T


```


```python linenums='1'
def positif(T):
    T2 = list(T)
    T3 = []
    while T2 != []:
        x = T2.pop()
        if x >= 0:
            T3.append(x)
    T2 = [] # <- NB : cette ligne est inutile
    while T3 != []:
        x = T3.pop()
        T2.append(x)
    print('T = ',T)
    return T2
```
```python linenums='1'
def liste_puissances(a, n):
    lst = [a]*n
    for i in range(1, n):
        lst[i] = a * lst[i-1]
    return lst

def liste_puissances_borne(a, borne):
    lst = []
    val = a
    while val < borne:
        lst.append(val)
        val = val * a
    return lst
```
```python linenums='1'
def liste_puissances(a,n):
    puissances = [a]
    for i in range(n-1):
        puissances.append(puissances[-1] * a)
    return puissances

def liste_puissances_borne(a, borne):
    lst = []
    val = a
    while val < borne:
        lst.append(val)
        val = val * a
    return lst
```
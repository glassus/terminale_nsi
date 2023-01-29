```python linenums='1'
def enumere(L):
    d = {}
    for i in range(len(L)):
        if L[i] in d:
            d[L[i]].append(i)
        else:
            d[L[i]] = [i]
    return d
```
```python linenums='1'
def convertir(tab):
    puissance = 0
    total = 0
    for i in range(len(tab)-1, -1, -1):
        total += tab[i]*(2**puissance)
        puissance += 1
    return total
```
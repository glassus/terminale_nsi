```python linenums='1'
def convertir(T):
    puissance = 0
    total = 0
    for i in range(len(T)-1, -1, -1):
        total += T[i]*(2**puissance)
        puissance += 1
    return total

```
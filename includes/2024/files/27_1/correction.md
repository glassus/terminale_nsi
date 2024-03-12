```python linenums='1'
def couples_consecutifs(tab):
    solution = []
    for i in range(len(tab)-1):
        if tab[i] + 1 == tab[i+1]:
            solution.append((tab[i], tab[i+1]))
    return solution

```
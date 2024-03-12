```python linenums='1'
from random import randint

def lancer(n):
    return [randint(1,6) for _ in range(n)]

def paire_6(tab):
    nb = 0
    for elt in tab:
        if elt == 6:
            nb += 1
    if nb >=2 :
        return True
    else:
        return False
```
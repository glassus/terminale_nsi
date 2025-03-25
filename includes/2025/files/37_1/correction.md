```python linenums='1'
def gb_vers_entier(tab):
    somme = 0
    for i in range(len(tab)):
        if tab[i]:
            somme += 2**(len(tab)-1-i)
    return somme 
```
```python linenums='1'
def ecriture_binaire_entier_positif(n):
    if n == 0:
        return '0' 
    bin_n = '' 
    while n != 0 : 
        bin_n = str(n % 2) + bin_n 
        n = n // 2
    return bin_n
```
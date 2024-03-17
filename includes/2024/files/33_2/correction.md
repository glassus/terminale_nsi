```python linenums='1' hl_lines='9 10 12 13'
ddef crible(n):
    """Renvoie un tableau contenant tous les nombres premiers
    plus petits que n."""
    premiers = []
    tab = [True] * n
    tab[0], tab[1] = False, False
    for i in range(n):
        if tab[i]:
            premiers.append(i)
            multiple = i 
            while multiple < n:
                tab[multiple] = False 
                multiple = multiple + i 
    return premiers


```
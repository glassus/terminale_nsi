Énoncé peu clair, on ne sait pas si ```n1``` et ```n2``` sont entiers naturels ou relatifs. Nous décidons qu'ils sont relatifs et donc qu'ils peuvent être négatifs, auquel cas on utilise le fait que $5 \\times (-6)= - (5 \\times 6)$.
```python linenums='1'
def multiplication(n1, n2):
    if n1 < 0:
        return -multiplication(-n1, n2)
    if n2 < 0:
        return -multiplication(n1, -n2)
    resultat = 0
    for _ in range(n2):
        resultat += n1
    return resultat
```
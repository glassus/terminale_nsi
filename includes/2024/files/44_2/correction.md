```python linenums='1' hl_lines='5 6 11'
def insere(arbre, cle):
""" arbre est une instance de la classe Arbre qui implémente
    un arbre binaire de recherche.
"""
    if cle < arbre.v:
        if arbre.fg is not None:
            insere(arbre.fg, cle)
        else:
            arbre.fg = Arbre(cle)
    else:
        if arbre.fd is not None:
            insere(arbre.fd, cle)
        else:
            arbre.fd = Arbre(cle)
```

Tests :

```python
>>> a = Arbre(5)
>>> insere(a, 2)
>>> insere(a, 7)
>>> insere(a, 3)
>>> parcours(a, [])
[2, 3, 5, 7]
>>> insere(a, 1)
>>> insere(a, 4)
>>> insere(a, 6)
>>> insere(a, 8)
>>> parcours(a, [])
[1, 2, 3, 4, 5, 6, 7, 8]
```
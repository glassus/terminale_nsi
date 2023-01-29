```python linenums='1'
def taille(a):
    if a is None:
        return 0
    else:
        return 1 + taille(a.fg) + taille(a.fd)
    
def hauteur(a):
    if a is None:
        return 0
    else:
        return 1 + max(hauteur(a.fg), hauteur(a.fd))
```

Tests :

```python
a = Arbre(0)
a.fg = Arbre(1)
a.fd = Arbre(2)
a.fg.fg = Arbre(3)
a.fd.fg = Arbre(4)
a.fd.fd = Arbre(5)
a.fd.fg.fd = Arbre(6)
```

```python
>>> taille(a)
7
>>> hauteur(a)
4
```
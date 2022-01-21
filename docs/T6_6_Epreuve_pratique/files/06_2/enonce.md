La fonction `recherche` prend en paramètres deux chaines de caractères `gene` et
`seq_adn` et renvoie `True` si on retrouve `gene` dans `seq_adn` et `False` sinon.
Compléter le code Python ci-dessous pour qu’il implémente la fonction `recherche`.

```python linenums='1'
def recherche(gene, seq_adn):
    n = len(seq_adn)
    g = len(gene)
    i = ...
    trouve = False
    while i < ... and trouve == ... :
        j = 0
        while j < g and gene[j] == seq_adn[i+j]:
            ...
        if j == g:
            trouve = True
        ...
    return trouve
```

Exemples :
```python
>>> recherche("AATC", "GTACAAATCTTGCC")
True
>>> recherche("AGTC", "GTACAAATCTTGCC")
False
```
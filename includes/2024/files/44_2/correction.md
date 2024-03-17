```python linenums='1' hl_lines='8 11'
def insere(arbre, cle):
    """insere la cle dans l'arbre binaire de recherche
    représenté par arbre.
    Retourne l'arbre modifié."""
    if arbre == None:
        return Noeud(cle, None, None) # creation d'une feuille
    else:
        if cle < arbre.etiquette: 
            arbre.gauche = insere(arbre.gauche, cle)
        else:
            arbre.droit = insere(arbre.droit, cle) 
        return arbre
```

Tests :

```python
>>> a = Noeud(5, None, None)
>>> a = insere(a, 2)
>>> a = insere(a, 3)
>>> a = insere(a, 7)
>>> parcours(a, [])
[2, 3, 5, 7]
>>> a = insere(a, 1)
>>> a = insere(a, 4)
>>> a = insere(a, 6)
>>> a = insere(a, 8)
>>> parcours(a, [])
[1, 2, 3, 4, 5, 6, 7, 8]
```
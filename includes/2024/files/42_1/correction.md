```python linenums='1'
def moyenne(tab):
    '''
    moyenne(list) -> float
    Entrée : un tableau non vide d'entiers
    Sortie : nombre de type float
    Correspondant à la moyenne des valeurs présentes dans le
    tableau
    '''
    somme = 0
    for elt in tab:
        somme += elt
    return somme / len(tab)
```
```python linenums='1' hl_lines='4 6 9 16 17 19 20'
urne = ['A', 'A', 'A', 'B', 'C', 'B', 'C', 'B', 'C', 'B']

def depouille(urne):
    resultat = {}
    for bulletin in urne:
        if bulletin in resultat:
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            resultat[bulletin] = 1
    return resultat

def vainqueur(election):
    vainqueur = '' #(1)
    nmax = 0
    for candidat in election:
        if election[candidat] > nmax :
            nmax = election[candidat]
            vainqueur = candidat #(2)
    liste_finale = [nom for nom in election if election[nom] == nmax]
    return liste_finale
```

1. Il est pourtant très déconseillé de nommer une variable avec le même nom que la fonction qui la contient...
2. Cette variable `vainqueur` est inutile, on ne s'en sert pas dans l'élaboration de la liste finale.
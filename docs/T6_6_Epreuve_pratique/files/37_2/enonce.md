Chaque soir, les auditeurs d’une radio votent en ligne pour leur artiste favori. Ces votes sont
stockés dans un tableau.

Exemple :

```python
Urne = ['Oreilles sales', 'Oreilles sales', 'Oreilles sales', 'Extra Vomit',
'Lady Baba', 'Extra Vomit', 'Lady Baba', 'Extra Vomit', 'Lady Baba', 'Extra Vomit']
```

La fonction `depouille` doit permettre de compter le nombre de votes exprimés pour chaque
artiste. Elle prend en paramètre un tableau et renvoie le résultat dans un dictionnaire dont les
clés sont les noms des artistes et les valeurs le nombre de votes en leur faveur.


La fonction vainqueur doit désigner le nom du ou des gagnants. Elle prend en paramètre un
dictionnaire dont la structure est celle du dictionnaire renvoyé par la fonction `depouille` et
renvoie un tableau. Ce tableau peut donc contenir plusieurs éléments s’il y a des artistes ex-
aequo.
Compléter les fonctions `depouille` et vainqueur ci-après pour qu’elles renvoient les
résultats attendus.

```python linenums='1'
urne = ['Oreilles sales', 'Oreilles sales', 'Oreilles sales',
      'Extra Vomit', 'Lady Baba', 'Extra Vomit', 'Lady Baba',
      'Extra Vomit', 'Lady Baba', 'Extra Vomit']

def depouille(urne):
    resultat = ...
    for bulletin in urne:
        if ...:
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            ...
    return resultat

def vainqueur(election):
    vainqueur = ''
    nmax = 0
    for candidat in election:
        if ... > ... :
            nmax = ...
            vainqueur = candidat
    liste_finale = [nom for nom in election if election[nom] == ...]
    return ...




```
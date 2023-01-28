La fonction `rendu_monnaie` prend en paramètres deux nombres entiers
positifs `somme_due` et `somme_versee` et elle permet de procéder au rendu de monnaie de la
différence `somme_versee – somme_due` pour des achats effectués avec le système de pièces de
la zone Euro. On utilise pour cela un algorithme glouton qui commence par rendre le maximum de
pièces de plus grandes valeurs et ainsi de suite. Par la suite, on
assimilera les billets à des pièces.


La fonction `rendu_monnaie` renvoie un tableau de type `list` contenant les pièces qui
composent le rendu.

Toutes les sommes sont exprimées en euros. Les valeurs possibles pour les
pièces sont donc `[1, 2, 5, 10, 20, 50, 100, 200]`.

Ainsi, l’instruction `rendu_monnaie(452, 500)`
renvoie le tableau
`[20, 20, 5, 2, 1]`.

En effet, la somme à rendre est de `48` euros soit `20 + 20 + 5 + 2 + 1`.

Le code de la fonction `rendu_monnaie` est donné ci-dessous :

```python linenums='1'
def rendu_monnaie(somme_due, somme_versee):
    pieces = [1, 2, 5, 10, 20, 50, 100, 200]
    rendu = ...
    a_rendre = ...
    i = len(pieces) - 1
    while a_rendre > ... :
        if pieces[i] <= a_rendre :
            rendu.append(...)
            a_rendre = ...
        else :
            i = ...
    return rendu
```

Compléter ce code et le tester :
```python
>>> rendu_monnaie(700,700)
[]
>>> rendu_monnaie(102,500)
[200, 100, 50, 20, 20, 5, 2, 1]
```
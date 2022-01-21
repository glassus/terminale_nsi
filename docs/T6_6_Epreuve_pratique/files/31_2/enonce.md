La fonction `rendu_monnaie_centimes` prend en paramètres deux nombres entiers
positifs `s_due` et` s_versee` et elle permet de procéder au rendu de monnaie de la
différence `s_versee – s_due` pour des achats effectués avec le système de pièces de
la zone Euro. On utilise pour cela un algorithme qui commence par rendre le maximum de
pièces de plus grandes valeurs et ainsi de suite. La fonction renvoie la liste des pièces qui
composent le rendu.

Toutes les sommes sont exprimées en centimes d’euros. Les valeurs possibles pour les
pièces sont donc `[1, 2, 5, 10, 20, 50, 100, 200]`.

Ainsi, l’instruction `rendu_monnaie_centimes(452, 500)`
renverra
`[20, 20, 5, 2, 1]`.

En effet, la somme à rendre est de `48` centimes soit `20 + 20 + 5 + 2 + 1`.
Le code de la fonction est donné ci-dessous :

```python linenums='1'
def rendu_monnaie_centimes(s_due, s_versee):
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

Compléter ce code pour qu'il donne :
```python
>>> rendu_monnaie_centimes(700,700)
[]
>>> rendu_monnaie_centimes(112,500)
[200, 100, 50, 20, 10, 5, 2, 1]
```
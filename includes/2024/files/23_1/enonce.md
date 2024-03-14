Dans cet exercice, on considère des arbres binaires de recherche qui sont :

- soit l’arbre vide identifié par `None` ;
- soit un nœud, contenant une clé et deux sous-arbres gauche et droit et représenté
par un triplet `(g, v, d)` où `g` et `d` sont les sous-arbres gauche et droit et `v` la clé.


![image](data2023/12_arbre.png){: .center width=30%}

Ainsi, l’arbre binaire de recherche `abr1` ci-
contre est créé par le code python ci-
dessous

```python
n0 = (None, 0, None)
n3 = (None, 3, None)
n2 = (None, 2, n3)
abr1 = (n0, 1, n2)
```

Écrire une fonction récursive `insertion_abr(a, cle)` qui prend en paramètres une
clé `cle` et un arbre binaire de recherche `a`, et qui renvoie un arbre binaire de recherche
dans lequel `cle` a été insérée.
Dans le cas où `cle` est déjà présente dans `a`, la fonction renvoie l’arbre a inchangé.

Résultats à obtenir :

```python
>>> insertion_abr(abr1, 4)
((None,0,None),1,(None,2,(None,3,(None,4,None))))
>>> insertion_abr(abr1, -5)
(((None,-5,None),0,None),1,(None,2,(None,3,None)))
>>> insertion_abr(abr1, 2)
((None,0,None),1,(None,2,(None,3,None)))
```
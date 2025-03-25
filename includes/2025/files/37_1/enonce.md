
On considère dans cet exercice une représentation binaire d’un entier non signé en tant que
tableau de booléens.
Si


```python
tab = [True, False, True, False, False, True, True]
```

est un tel tableau, alors l’entier qu’il représente est $2^6 +2^4 + 2^1 + 2^0 = 83$. Cette représentation consistant à placer en premier le booléen indiquant la puissance la plus élevée de 2
est dite *big-endian* ou grand-boutiste.


Écrire une fonction `gb_vers_entier` qui prend en paramètre un tel tableau et renvoie
l’entier qu’il représente.


Exemple :

```python
>>> gb_vers_entier([])
0
>>> gb_vers_entier([True])
1
>>> gb_vers_entier([True, False, True, False, False, True, True])
83
>>> gb_vers_entier([True, False, False, False, False, False, True, False])
130
```
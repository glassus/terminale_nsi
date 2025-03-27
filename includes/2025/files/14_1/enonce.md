Dans cet exercice les tableaux sont représentés par des listes Python (type `list`).

Écrire en python deux fonctions :

- `lancer` de paramètre `n`, un entier positif, qui renvoie un tableau de `n` entiers obtenus
aléatoirement entre 1 et 6 (1 et 6 inclus) ;
- `paire_6` de paramètre `tab`, un tableau de n entiers compris entre 1 et 6 et qui
renvoie un booléen égal à `True` si le nombre de 6 est supérieur ou égal à 2, `False`
sinon.


On pourra utiliser la fonction `randint(a,b)` du module `random` pour laquelle la
documentation officielle est la suivante :

`random.randint(a, b)`
`      Renvoie un entier aléatoire N tel que a <=N <= b.`

Exemples :

```python
>>> lancer1 = lancer(5)
>>> lancer1
[5, 6, 6, 2, 2]
>>> paire_6(lancer1)
True
>>> lancer2 = lancer(5)
>>> lancer2
[6, 5, 1, 6, 6]
>>> paire_6(lancer2)
True
>>> lancer3 = lancer(3)
>>> lancer3
[2, 2, 6]
>>> paire_6(lancer3)
False
>>> lancer4 = lancer(0)
>>> lancer4
[]
>>> paire_6(lancer4)
False
```
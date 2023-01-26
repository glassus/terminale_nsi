On s’intéresse au problème du rendu de monnaie. On suppose qu’on dispose d’un
nombre infini de billets de 5 euros, de pièces de 2 euros et de pièces de 1 euro.
Le but est d’écrire une fonction nommée `rendu` dont le paramètre est un entier positif non
nul `somme_a_rendre` et qui retourne une liste de trois entiers `n1`, `n2` et `n3` qui
correspondent aux nombres de billets de 5 euros (`n1`) de pièces de 2 euros (`n2`) et de
pièces de 1 euro (`n3`) à rendre afin que le total rendu soit égal à `somme_a_rendre`.

On utilisera un algorithme glouton : on commencera par rendre le nombre maximal de
billets de 5 euros, puis celui des pièces de 2 euros et enfin celui des pièces de 1 euros.

Exemples :
```python
>>> rendu(13)
[2,1,1]
>>> rendu(64)
[12,2,0]
>>> rendu(89)
[17,2,0]
```
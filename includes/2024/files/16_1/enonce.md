Écrire une fonction `ecriture_binaire_entier_positif` qui prend en paramètre un
entier positif `n` et renvoie une une chaine de caractère correspondant à l‘écriture binaire de `n`.


On rappelle que :

- l’écriture binaire de 25 est 11001 car $25 = 1 \times 2^4 + 1 \times 2^3 + 0 \times 2^2 + 0 \times 2^1 + 1 \times 2^0$ ;
- `n % 2` vaut 0 ou 1 selon que `n` est pair ou impair ;
- `n // 2`  donne le quotient de la division euclidienne de `n` par 2.


Il est interdit dans cet exercice d’utiliser la fonction `bin` de Python.


Exemples :

```python
>>> 5 % 2
1
>>> 5 // 2
2
>>> ecriture_binaire_entier_positif(0)
'0'
>>> ecriture_binaire_entier_positif(2)
'10'
>>> ecriture_binaire_entier_positif(105)
'1101001'
```

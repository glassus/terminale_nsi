On considère la fonction `dec_to_bin` ci-dessous qui prend en paramètre un entier positif `a` en écriture décimale et qui renvoie son écriture binaire sous la forme d'une chaine de caractères.

```python linenums='1'
def dec_to_bin(a):
    bin_a = ...
    a = a//2
    while a ... :
        bin_a = ... + bin_a
        a = ...
    return bin_a
```
Compléter la fonction `dec_to_bin`.

Exemples :
```python
>>> dec_to_bin(83)
'1010011'
>>> dec_to_bin(127)
'1111111'
```
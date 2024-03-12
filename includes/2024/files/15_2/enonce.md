On considère la fonction `binaire` ci-dessous qui prend en paramètre un entier positif `a` en écriture décimale et qui renvoie son écriture binaire sous la forme d'une chaine de caractères.

L’algorithme utilise la méthode des divisions euclidiennes successives comme l’illustre
l’exemple ci-après.

![image](data2023/30_divisions.png){: .center}



```python linenums='1'
def binaire(a):
    bin_a = ...
    a = a // 2
    while a ... :
        bin_a = ... + bin_a
        a = ...
    return bin_a
```
Compléter le code de la fonction `binaire`.

Exemples :
```python
>>> binaire(83)
'1010011'
>>> binaire(127)
'1111111'
>>> binaire(0)
'0'
```
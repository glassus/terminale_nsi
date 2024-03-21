L’objectif de cet exercice est d’écrire deux fonctions récursives `dec_to_bin` et
`bin_to_dec` assurant respectivement la conversion de l’écriture décimale d’un nombre
entier vers son écriture en binaire et, réciproquement, la conversion de l’écriture en
binaire d’un nombre vers son écriture décimale.

Dans cet exercice, on s’interdit l’usage des fonctions Python `bin` et `int`.

L'exemple suivant montre comment obtenir l’écriture en binaire du
nombre 25 :

$25 =  2 \times 12 + 1$  
$\phantom{25} = 2 \times (2 \times 6 + 0) + 1$  
$\phantom{25} = 2 \times (2 \times (2 \times 3 + 0) + 0) + 1$  
$\phantom{25} = 2 \times (2 \times (2 \times (2 \times 1+1) + 0) + 0) + 1$     
$\phantom{25} = 2 \times (2 \times (2 \times (2 \times (2 \times 0 + 1)+1) + 0) + 0) + 1$   
$\phantom{25} = 1 \times 2^4 + 1 \times 2^3 + 0 \times 2^2 + 0 \times 2^1 + 1 \times 2^0$   

L'écriture binaire de 25 est donc ```11001```.

0n rappelle également que :

- `a // 2` renvoie le quotient de la division euclidienne de `a` par 2.
- ` a % 2` renvoie le reste dans la division euclidienne de `a` par 2.

On indique enfin qu’en Python si `mot = "informatique"` alors :

- `mot[-1]` renvoie `'e'`, c’est-à-dire le dernier caractère de la chaîne de caractères `mot`.
- `mot[:-1]` renvoie `'informatiqu'` , c’est-à-dire l’ensemble de la chaîne de
caractères `mot` privée de son dernier caractère.

Compléter, puis tester, les codes de deux fonctions ci-dessous. 
On précise que la fonction récursive `dec_to_bin` prend en paramètre un nombre entier
et renvoie une chaîne de caractères contenant l’écriture en binaire du nombre passé en
paramètre.

Exemple :

```python
>>> dec_to_bin(25)
'11001'
```


La fonction récursive `bin_to_dec` prend en paramètre une chaîne de caractères
représentant l’écriture d’un nombre en binaire et renvoie l’écriture décimale de ce
nombre.

```python
>>> bin_to_dec('101010')
42
```


```python linenums='1'
def dec_to_bin(nb_dec):
    q, r = nb_dec // 2, nb_dec % 2
    if q == ...: 
        return ... 
    else:
        return dec_to_bin(...) + ... 

def bin_to_dec(nb_bin):
    if len(nb_bin) == 1:
        if ... == '0': 
            return 0
        else:
            return ... 
    else:
        if nb_bin[-1] == '0':
            bit_droit = 0
        else:
            ...
        return ... * bin_to_dec(nb_bin[:-1]) + ... 
```
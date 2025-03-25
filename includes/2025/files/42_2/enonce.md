Pour rappel, la conversion d’un nombre entier positif en binaire peut s’effectuer à l’aide
des divisions successives comme illustré ici :

![image](data2023/31_divisions.png){: .center}

Voici une fonction Python basée sur la méthode des divisions successives permettant de
convertir un nombre entier positif en binaire :

Compléter la fonction ```binaire```

```python linenums='1'
def binaire(a):
    '''convertit un nombre entier a en sa representation 
    binaire sous forme de chaine de caractères.'''
    if a == 0:
        return '0'
    bin_a = ... 
    while ...: 
        bin_a = ... + bin_a 
        a = ... 
    return bin_a

```
.

Exemples :

```python
>>> binaire(0)
'0'
>>> binaire(77)
'1001101'
```
Pour rappel, la conversion d’un nombre entier positif en binaire peut s’effectuer à l’aide
des divisions successives comme illustré ici :

![image](data/img21_2.png){: .center}

Voici une fonction Python basée sur la méthode des divisions successives permettant de
convertir un nombre entier positif en binaire :
```python linenums='1'
def binaire(a):
    bin_a = str(...)
    a = a // 2
    while a ... :
        bin_a = ...(a%2) + ...
        a = ...
    return bin_a
```
Compléter la fonction ```binaire```.

Exemples :

```python
>>> binaire(0)
'0'
>>> binaire(77)
'1001101'
```
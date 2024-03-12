Le codage de César transforme un message en changeant chaque lettre en la décalant
dans l’alphabet.
Par exemple, avec un décalage de 3, le A se transforme en D, le B en E, ..., le X en A,
le Y en B et le Z en C. Les autres caractères (‘!’,’ ?’ ...) ne sont pas codés.

La fonction `position_alphabet` ci-dessous prend en paramètre un caractère `lettre`
et renvoie la position de `lettre` dans la chaîne de caractères `ALPHABET` s’il s’y trouve.

La fonction `cesar` prend en paramètre une chaîne de caractères `message` et un nombre
entier `decalage` et renvoie le nouveau message codé avec le codage de César utilisant
le décalage `decalage`.

```python linenums='1'
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def position_alphabet(lettre):
    return ord(lettre) - ord('A')

def cesar(message, decalage):
    resultat = ''
    for ... in message:
        if 'A' <= c and c <= 'Z':
            indice = ( ... ) % 26
            resultat = resultat + ALPHABET[indice]
        else:
            resultat = ...
    return resultat
```

Compléter la fonction ```cesar```.

Exemples :

```python
>>> cesar('BONJOUR A TOUS. VIVE LA MATIERE NSI !', 4)
'FSRNSYV E XSYW. ZMZI PE QEXMIVI RWM !'
>>> cesar('GTSOTZW F YTZX. ANAJ QF RFYNJWJ SXN !', -5)
'BONJOUR A TOUS. VIVE LA MATIERE NSI !'
``` 
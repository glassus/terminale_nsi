```python linenums='1'
def inverse_chaine(chaine):
    result = ''
    for caractere in chaine:
        result = caractere + result
    return result

def est_palindrome(chaine):
    inverse = inverse_chaine(chaine)
    return chaine == inverse

def est_nbre_palindrome(nbre):
    chaine = str(nbre)
    return est_palindrome(chaine)

```
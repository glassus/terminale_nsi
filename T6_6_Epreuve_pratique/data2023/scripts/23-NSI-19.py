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

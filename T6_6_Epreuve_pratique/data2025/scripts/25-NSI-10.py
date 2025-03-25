alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def position_alphabet(lettre):
    '''Renvoie la position de la lettre dans l'alphabet'''
    return ord(lettre) - ord('A')

def cesar(message, decalage):
    '''Renvoie le message codé par la méthode de César
    pour le decalage donné'''
    resultat = ''
    for ... in message: 
        if 'A' <= c and c <= 'Z':
            indice = (...) % 26 
            resultat = resultat + alphabet[indice]
        else:
            resultat = ... 
    return resultat



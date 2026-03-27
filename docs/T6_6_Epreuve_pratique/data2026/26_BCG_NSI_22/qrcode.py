import ascii

#############################################################################
# Question 1 et 2 : Écrire les codes des fonctions bin2dec et qrcode2dec
#              Proposer un test de qrcode2dec    
#############################################################################


# implémentation du QR Code de la figure 1:
qrcode_fig1 = ascii.figure1



#############################################################################
# Question 3 : Fonctions dec2str et test_dec2str                             
#############################################################################
def dec2str(liste_dec):
    """ entrée: liste d'entiers décimaux
        sortie: chaine de caractère formée des caractères correspondant
        de la table ascii """
    table_ascii = ascii.dict_ascii
    chaine = ""
    for entier in liste_dec:
        chaine += table_ascii[entier]
    return chaine
        
def test_dec2str():
    """ Teste la fonction dec2str avec des données issues du module fourni """
    tests = [ascii.test1, ascii.test2, ascii.test3]
    for test in tests:
        print(dec2str(test))

def qrcode2str(qrcode):
    return dec2str(qrcode2dec(qrcode))

#############################################################################
# Question 4 : Fonction str2qrcode déficiente
#############################################################################

def str2qrcode(message):
    """
    Convertit une chaine de caractères en liste de tuples binaires.
    """
    qrcode = []
    table_inverse = {valeur: cle for cle, valeur in ascii.dict_ascii.items()}

    for caractere in message:
        entier = table_inverse.get(caractere, 63)
        binaire_str = bin(entier)[2:]
        ligne = tuple(int(bit) for bit in binaire_str)
        qrcode.append(ligne)
        
    return qrcode

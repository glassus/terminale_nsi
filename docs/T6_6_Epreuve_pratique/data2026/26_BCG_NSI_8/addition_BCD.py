#############################################################################
# Question 1 : Mise en évidence du problème des flottants                   #
#############################################################################
# Écrire ci-dessous la fonction calcul_recettes() et son appel


#############################################################################
# Question 2 : Conversion BCD vers Décimal                                  #
#############################################################################
# Écrire ci-dessous la fonction convertir_BCD_vers_decimal(liste_quartets)
# et l'assertion de test demandée


#############################################################################
# Code fourni pour les questions 3 et 4                                     #
#############################################################################

def convertir_dec_vers_BCD(decimal):
    """
    Convertit une chaîne représentant un décimal vers une liste de quartets BCD.
    Convention : virgule implicite avant les deux derniers quartets.
    """
    ajouter_zero = False
    liste_quartets = []

    if '.' not in decimal:
        decimal = decimal + '.00'

    for i in range(len(decimal)):
        if decimal[i] != '.':
            quartet = bin(int(decimal[i]))[2:].zfill(4)
            liste_quartets.append(quartet)

        # Si le nombre n'a qu'un seul chiffre après la virgule
        if decimal[i] == '.' and i == len(decimal) - 2:
            ajouter_zero = True

    if ajouter_zero:
        liste_quartets.append('0000')

    return liste_quartets


def additionner_binaire_quartets(quartet1, quartet2, retenue):
    """
    Additionne bit à bit deux quartets binaire purs.
    Renvoie un tuple (somme_binaire_str, nouvelle_retenue_int).
    """
    somme = ""
    for i in range(4):
        # Lecture de la droite vers la gauche
        bit1 = int(quartet1[3 - i])
        bit2 = int(quartet2[3 - i])
        total = bit1 + bit2 + retenue

        if total == 0:
            somme = '0' + somme
            retenue = 0
        elif total == 1:
            somme = '1' + somme
            retenue = 0
        elif total == 2:
            somme = '0' + somme
            retenue = 1
        elif total == 3:
            somme = '1' + somme
            retenue = 1

    return somme, retenue


def corriger_BCD(somme, retenue):
    """
    Applique la correction BCD si le quartet dépasse 9 ou génère une retenue.
    Ajoute '0110' (6) au quartet invalide.
    """
    # Si somme >= 10 ('1010' ou '1011' ou '1100' etc.)
    if somme[0] == '1' and (somme[1] == '1' or somme[2] == '1'):
        somme, retenue = additionner_binaire_quartets(somme, '0110', 0)
        return somme, retenue

    # S'il y a eu dépassement naturel lors de l'addition binaire
    if retenue == 1:
        somme, _ = additionner_binaire_quartets(somme, '0110', 0)
        return somme, retenue
        
    return somme, retenue


def aligner_quartets(q1: list, q2: list) -> tuple:
    """
    Doit équilibrer les deux listes en ajoutant des '0000' à gauche 
    de la liste la plus courte.
    """
    return q1, q2


def additionner_nombres_format_BCD(a, b):
    """
    Additionne deux nombres au format BCD, quartet par quartet.
    """
    liste_quartets1 = convertir_dec_vers_BCD(a)
    liste_quartets2 = convertir_dec_vers_BCD(b)

    # Ajustement de la longueur
    liste_quartets1, liste_quartets2 = aligner_quartets(liste_quartets1, liste_quartets2)

    retenue = 0
    resultat = []
    longueur_max = max(len(liste_quartets1), len(liste_quartets2)) 

    for i in range(longueur_max):
        index = longueur_max - i - 1
        
        # Addition binaire simple des quartets
        somme, retenue = additionner_binaire_quartets(liste_quartets1[index], liste_quartets2[index], retenue)
        
        resultat.insert(0, somme) 

    # Gestion de la dernière retenue éventuelle
    if retenue == 1:
        resultat.insert(0, '0001')
        
    return resultat
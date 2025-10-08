from PIL import Image

def codage_rle(liste_octets):
    '''Renvoie une liste d'octets obtenue par compression RLE'''
    liste_rle = []
    i = 0
    while i < len(liste_octets):
        c = liste_octets[i]
        k = 1
        while i+k < len(liste_octets) and liste_octets[i+k] == c:
            k += 1
        liste_rle.append(k)
        liste_rle.append(c)
        i += k
    return liste_rle

def decodage_rle(liste_rle):
    '''Renvoie la liste d'octets obtenue à partir de la liste liste_rle obtenue
    par compression RLE'''
    # A VOUS D'ÉCRIRE LE CODE LA FONCTION

def test_codage():
    assert codage_rle([255, 255, 0, 255, 255, 255]) == [2, 255, 1, 0, 3, 255]
    assert decodage_rle([2, 255, 1, 0, 3, 255]) == [255, 255, 0, 255, 255, 255]

#############################################################################
# Il n'est pas nécessaire de comprendre le code de ces 4 fonctions, mais il # 
# sera nécessaire de les utiliser dans la suite à partir de l'exemple.      #
#############################################################################

def enregistrer_octets(nom_fichier, liste_octets):
    '''Enregistre une liste de valeurs numériques entre 0 et 255 dans un
    le fichier nom_fichier. Si une valeur est plus grande que 255 on considère
    que c'est 255. De même pour les valeur plus petite que 0.'''
    with open(nom_fichier, 'wb') as fichier:
        fichier.write(bytes([ max(0, min(255, b)) for b in liste_octets]))

def charger_octets(nom_fichier):
    '''Renvoie la liste des octets présents dans le fichier nom_fichier'''
    with open(nom_fichier, 'rb') as fichier:
        liste_octets = list(fichier.read())
        return liste_octets

def enregistrer_image(nom_image, largeur, liste_niveaux):
    '''Enregistre un fichier image nom_image de la largeur donnée et dont les 
    valeurs de niveaux de gris des pixels sont celles de la liste
    liste_niveaux'''
    hauteur = len(liste_niveaux) // largeur
    im = Image.frombytes('L', (largeur, hauteur), bytes(liste_niveaux))
    im.save(nom_image)

def charger_image(nom_image):
    '''Étant donné une image nom_image, renvoie un couple (largeur, liste_niveaux) où 
    largeur est la largeur de l'image et liste_niveaux est la liste des valeurs de niveaux 
    de gris de l'image ligne par ligne'''

    image = Image.open(nom_image).convert('L')
    return (image.width, list(image.tobytes()))

#############################################################################
# Fonction nécessaire pour les tests de la question 3                       #
#############################################################################

def encoder_decoder_image(nom_image):
    '''Fonction de test permettant d'encoder puis décoder une image avec un
    codage RLE. Le fichier rle est nommé nom_image.rle et le fichier decodé
    est nom_image.dec.png'''
    w, l = charger_image(nom_image)
    enregistrer_octets(nom_image+'.rle', codage_rle(l))
    l = charger_octets(nom_image+'.rle')
    enregistrer_image(nom_image+'.dec.png', w, decodage_rle(l))


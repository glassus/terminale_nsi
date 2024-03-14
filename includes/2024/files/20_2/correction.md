```python linenums='1' hl_lines='3 7 18 19 30 31 32 34'
def nombre_lignes(image):
    '''renvoie le nombre de lignes de l'image'''
    return len(image) 

def nombre_colonnes(image):
    '''renvoie la largeur de l'image'''
    return len(image[0]) 

def negatif(image):
    '''renvoie le negatif de l'image sous la forme
       d'une liste de listes'''
    # on cree une image de 0 aux memes dimensions 
    # que le parametre image
    nouvelle_image = [[0 for k in range(nombre_colonnes(image))]
         for i in range(nombre_lignes(image))]

    for i in range(nombre_lignes(image)):
        for j in range(nombre_colonnes(image)): 
            nouvelle_image[i][j] = 255 - image[i][j] 
    return nouvelle_image

def binaire(image, seuil):
    '''renvoie une image binarisee de l'image sous la forme
       d'une liste de listes contenant des 0 si la valeur
       du pixel est strictement inferieure au seuil et 1 sinon'''
    nouvelle_image = [[0] * nombre_colonnes(image)
                      for i in range(nombre_lignes(image))]

    for i in range(nombre_lignes(image)):
        for j in range(nombre_colonnes(image)): 
            if image[i][j] < seuil : 
                nouvelle_image[i][j] = 0 
            else:
                nouvelle_image[i][j] = 1 
    return nouvelle_image
```
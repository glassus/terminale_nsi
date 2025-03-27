On considère une image en 256 niveaux de gris que l’on représente par une grille de
nombres, c’est-à-dire une liste composée de sous-listes toutes de longueurs identiques.


La largeur de l’image est donc la longueur d’une sous-liste et la hauteur de l’image est le
nombre de sous-listes.


Chaque sous-liste représente une ligne de l’image et chaque élément des sous-listes est
un entier compris entre 0 et 255, représentant l’intensité lumineuse du pixel.


Le négatif d’une image est l’image constituée des pixels `x_n` tels que
`x_n + x_i = 255` où `x_i` est le pixel correspondant de l’image initiale.

Étant donné une valeur `seuil`, la binarisation d'une image est l'image constituée des pixels `x_b` valant `0` si `x_i < seuil` et `255` sinon, où `x_i` est le pixel correspondant de l'image initiale.

Compléter le programme suivant :
```python linenums='1'
def nombre_lignes(image):
    '''renvoie le nombre de lignes de l'image'''
    return ... 

def nombre_colonnes(image):
    '''renvoie la largeur de l'image'''
    return ... 

def negatif(image):
    '''renvoie le negatif de l'image sous la forme
       d'une liste de listes'''
    # on cree une image de 0 aux memes dimensions 
    # que le parametre image
    nouvelle_image = [[0 for k in range(nombre_colonnes(image))]
         for i in range(nombre_lignes(image))]

    for i in range(nombre_lignes(image)):
        for j in range(...): 
            nouvelle_image[i][j] = ... 
    return nouvelle_image

def binaire(image, seuil):
    '''renvoie une image binarisee de l'image sous la forme
       d'une liste de listes contenant des 0 si la valeur
       du pixel est strictement inferieure au seuil et 255 sinon'''
    nouvelle_image = [[0] * nombre_colonnes(image)
                      for i in range(nombre_lignes(image))]

    for i in range(nombre_lignes(image)):
        for j in range(...): 
            if image[i][j] < ... : 
                nouvelle_image[i][j] = ... 
            else:
                nouvelle_image[i][j] = ... 
    return nouvelle_image





```

**Exemples :**

```python
>>> img=[[20, 34, 254, 145, 6], [23, 124, 237, 225, 69],
[197, 174, 207, 25, 87], [255, 0, 24, 197, 189]]
>>> nombre_lignes(img)
4
>>> nombre_colonnes(img)
5
>>> negatif(img)
[[235, 221, 1, 110, 249], [232, 131, 18, 30, 186],
[58, 81, 48, 230, 168], [0, 255, 231, 58, 66]]
>>> binaire(img,120)
[[0, 0, 255, 255, 0],[0, 255, 255, 255, 0],
[255, 255, 255, 0, 0],[255, 0, 0, 255, 255]]
```


coeur = [[0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
         [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
         [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]]

def affiche(dessin):
    ''' affichage d'une grille : les 1 sont représentés par 
        un "*" , les 0 par une espace " " '''
    for ligne in dessin:
        affichage = ''
        for col in ligne:
            if col == 1:
                affichage = affichage + "*"
            else:
                affichage = affichage + " "
        print(affichage)


def liste_zoom(liste_depart,k):
    '''renvoie une liste contenant k fois chaque élément de
       liste_depart'''
    liste_zoomee = ... 
    for elt in ... : 
        for i in range(k):
            ...
    return liste_zoomee

def dessin_zoom(grille,k):
    '''renvoie une grille où les lignes sont zoomées k fois 
       ET répétées k fois'''
    grille_zoomee=[]
    for ligne in grille:
        ligne_zoomee = ... 
        for i in range(k):
            ... .append(...) 
    return grille_zoomee



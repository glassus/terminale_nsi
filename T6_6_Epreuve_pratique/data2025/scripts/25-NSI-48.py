def distance_carre(point1, point2):
    """ Calcule et renvoie la distance au carre entre 
    deux points."""
    return (...)**2 + (...)**2 

def point_le_plus_proche(depart, tab):
    """ Renvoie les coordonnées du premier point du tableau tab se 
    trouvant à la plus courte distance du point depart."""
    min_point = tab[0]
    min_dist = ... 
    for i in range(1, len(tab)):
        if distance_carre(tab[i], depart) < ...: 
            min_point = ... 
            min_dist = ... 
    return min_point



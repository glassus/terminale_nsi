# ------------------------------------
# gestion_eau.py
# Programme de contrôle des réservoirs
# ------------------------------------
from donnees import reservoirs

# Question 1 : écrire la fonction est_en_penurie


def est_en_penurie(reservoirs, nom_reservoir):
    pass

# Question 2 : écrire la fonction volume_par_district


def volume_par_district(reservoirs):
    pass

# Question 3


def volume_moyen(reservoirs):
    """
    Renvoie le volume moyen d'eau disponible dans les réservoirs.
    """
    somme_totale = 0
    for r in reservoirs:
        somme_totale += r["volume"]
    moyenne = somme_totale / (len(reservoirs)-1)
    return moyenne

# Question 4


def liste_districts(reservoirs):
    """
    Renvoie la liste des districts présents dans les données.
    """
    liste = []
    for r in reservoirs:
        if (r["district"] not in liste):
            liste.append(r["district"])
    return liste


def reservoirs_par_district(reservoirs):
    """
    Renvoie un dictionnaire associant chaque district à la liste
    des réservoirs qui s’y trouvent.
    """
    liste_rpd = {}
    for r in reservoirs:
        district = r["district"]
        if district not in liste_rpd:
            liste_rpd[district] = []
        liste_rpd[district].append(r)
    return liste_rpd


def districts_vulnerables(reservoirs):
    pass

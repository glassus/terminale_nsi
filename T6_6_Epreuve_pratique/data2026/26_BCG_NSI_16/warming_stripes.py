import csv
import matplotlib.pyplot as plt

############ Question 1  ############


def charger(nom_fichier):
    """
    Lit un fichier CSV (contenant les colonnes 'Year' et 'Anomaly') 
    et renvoie une liste de dictionnaires correctement typés.
    """
    donnees = []
    with open(nom_fichier, mode='r', encoding='utf-8') as f:
        lecteur = csv.DictReader(f)
        for ligne in lecteur:
            annee = int(ligne["Year"])
            ecart = float(ligne["Anomaly"])
            donnees.append({"année": annee, "écart": ecart})
    return donnees


# Chargement global des données
datas_temperature = charger("datas.csv")

#############################################################################
# Question 1 : Recherche de l'écart                                         #
#############################################################################

# Écrire la fonction ecart_temperature et ses tests ici


def derniere_annee_ecart_negatif(datas):
    annee = max([element["année"] for element in datas])
    ecart = ecart_temperature(datas, annee)
    while ecart >= 0:
        annee = annee - 1
        ecart = ecart_temperature(datas, annee)
    return annee


#############################################################################
# Question 2 : Analyse et correction de bug                                 #
#############################################################################

def moyenne_ecarts(annee_debut, annee_fin, datas):
    """
    Renvoie la moyenne des écarts de température pour la période comprise 
    entre annee_debut et annee_fin (incluses).
    """
    somme = 0
    compteur = 0
    for dico in datas:
        if annee_debut <= dico["année"] and dico["année"] <= annee_fin:
            somme = somme - dico["écart"]
            compteur += 1
    return somme / compteur


def prevision(datas, annee, n):
    """
    Renvoie l'écart de température attendu calculé par régression linéaire 
    sur les n dernières années.
    """
    longueur = len(datas)
    annee_debut = datas[longueur-n]["année"]
    annee_fin = datas[longueur-1]["année"]

    moy_annees = (annee_debut + annee_fin) / 2
    moy_temperatures = moyenne_ecarts(annee_debut, annee_fin, datas)

    numerateur = 0
    denominateur = 0
    for i in range(1, n+1):
        ecart_annee = datas[longueur-i]["année"] - moy_annees
        ecart_temp = datas[longueur-i]["écart"] - moy_temperatures
        numerateur += ecart_annee * ecart_temp
        denominateur += ecart_annee ** 2

    a = numerateur / denominateur
    b = moy_temperatures - a * moy_annees

    return a * annee + b

# print("Prévision pour 2040 :", prevision(datas_temperature, 2040, 20))


#############################################################################
# Question 3 : Dataviz (Warming Stripes)                                    #
#############################################################################

def graphique(datas):
    """
    Représente visuellement les warming stripes.
    """
    fig, ax = plt.subplots(figsize=(10, 2))

    # Création d'une palette de couleurs basée sur l'amplitude thermique
    cmap = plt.get_cmap("seismic")
    temperatures = [dico["écart"] for dico in datas]
    max_val = max(max(temperatures), -min(temperatures))
    norm = plt.Normalize(-max_val, max_val)

    # Création des listes pour les abscisses et ordonnées
    annees = []
    ordonnees = []

    # Remplir les listes annees et ordonnees ici :

    # Génération du graphique
    ax.bar(annees, ordonnees, width=1.0, color=cmap(norm(temperatures)))
    ax.set_title("Warming Stripes mondiales - Base 1901-2000")
    plt.yticks([], [])  # Masque l'axe Y car seule la couleur compte
    ax.set_xlabel("Année")

    plt.tight_layout()
    plt.show()

# graphique(datas_temperature)
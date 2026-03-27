class Plante:
    def __init__(self, nom, espece, croissance, taille, exposition):
        self.nom = nom
        self.espece = espece
        self.croissance = croissance  # en jours
        self.taille = taille          # en cm
        self.exposition = exposition  # type d'exposition

plantes = [
    Plante("Basilic", "Ocimum basilicum", 60, 40, "plein soleil"),
    Plante("Tomate", "Solanum lycopersicum", 80, 100, "plein soleil"),
    Plante("Menthe", "Mentha spicata", 80, 50, "mi-ombre"),
    Plante("Tournesol", "Helianthus annuus", 85, 200, "plein soleil"),
    Plante("Fougère", "Dryopteris filix-mas", 90, 80, "ombre")
]
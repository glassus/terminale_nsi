import matplotlib.pyplot as plt
from transmission import Transmission

# Extraction des données
with open("data.txt", "r") as f:
    trames = f.read().split("\n")
    trames.pop()  # La dernière ligne est vide, on la supprime

# Création d'une liste de températures pour les transmissions valides
transmissions = [Transmission(t) for t in trames]
temperatures = [t.get_temperature() for t in transmissions if t.est_valide()]

print(f"Nombre de trames reçues : {len(trames)}")
print(f"Nombre de trames valides : {len(temperatures)}")

# Affichage des températures
plt.figure(figsize=(10, 5))
plt.plot(temperatures, label="Température (°C)")
plt.title("Évolution de la température")
plt.xlabel("Mesures")
plt.ylabel("Température (°C)")
plt.legend()
plt.grid(True)
plt.show()

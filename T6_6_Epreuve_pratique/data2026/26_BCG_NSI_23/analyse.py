import matplotlib.pyplot as plt
from Transmission import Transmission

# Extraction des données

with open("data.txt", "r") as f:
	trames = f.read().split("\n")
	trames.pop() # La dernière ligne est vide, on la supprime
	
# Création d'une liste de températures

transmissions = [Transmission(t) for t in trames]
temperatures = [t.get_temperature() for t in transmissions if t.est_valide()]

# Affichage des températures

plt.plot(temperatures)
plt.show()

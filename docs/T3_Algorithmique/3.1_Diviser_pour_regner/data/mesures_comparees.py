import time

import matplotlib.pyplot as plt

def puissance(a, n):
    if n == 0:
        return 1
    else:
        return a * puissance(a, n-1)
    
def puissance_mod(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return puissance_mod(a*a, n//2)
    else:
        return a * puissance_mod(a*a, (n-1)//2)


def mesure(n):
    t0 = time.time()
    h = puissance(3,n)
    return time.time() - t0

def mesure_mod(n):
    t0 = time.time()
    h = puissance_mod(3,n)
    return time.time() - t0


def moy_mesure(n, nb):
    s = []
    for k in range(nb):
        s.append(mesure(n))
    s.sort()
    ns = s[10:40]
    return sum(ns)/len(ns)

nmes = 100
sig = 10

def moy_mesure_mod(n, nb):
    s = []
    for k in range(nb):
        s.append(mesure_mod(n))
    s.sort()
    delta = int(nmes*sig/100)
    
    k1 = delta
    k2 = nmes - delta
    ns = s[k1:k2]
    return sum(ns)/len(ns)

x = list(range(200))
y = [moy_mesure(mx,nmes) for mx in x]
y_mod = [moy_mesure_mod(mx,nmes) for mx in x]
plt.plot(x,y, label = "puissance(3, n)")
plt.plot(x,y_mod,  label = "puissance_mod(3, n)")
plt.legend(loc="upper left")
plt.xlabel("valeur de l'exposant n")
plt.ylabel("temps moyen (s)")
plt.title("Comparaison du temps moyen d'exécution")
plt.show()
plt.save("test.png")

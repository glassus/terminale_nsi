```python linenums='1'
def ou_exclusif(tab1, tab2):
    resultat = []
    taille = len(tab1)
    for i in range(taille):
        resultat.append(tab1[i] ^ tab2[i])
    return resultat
```

Si on ne connait pas la fonction native ^ qui fait le «ou exclusif» de deux entiers en Python, on peut la recoder :

```python linenums='1'
def ou_exc(a, b):
    if a == 0 and b == 0:
        return 0
    if a == 0 and b == 1:
        return 1
    if a == 1 and b == 0:
        return 1
    if a == 1 and b == 1:
        return 0
```

Le code devient alors :

```python linenums='1'
def ou_exclusif(tab1, tab2):
    resultat = []
    taille = len(tab1)
    for i in range(taille):
        resultat.append(ou_exc(tab1[i],tab2[i]))
    return resultat
```
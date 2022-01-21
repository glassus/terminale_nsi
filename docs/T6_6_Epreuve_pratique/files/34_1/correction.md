```python linenums='1'
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o,','p','q','r','s','t','u','v','w','x','y','z']

def occurrence_max(chaine):
    occurence = [0] *  26
    for i in range(26):
        compteur = 0
        for caractere in chaine:
            if caractere == alphabet[i]:
                compteur += 1
        occurence[i] = compteur
    ind_max = 0
    for i in range(26):
        if occurence[i] > occurence[ind_max]:
            ind_max = i
    return alphabet[ind_max]
```
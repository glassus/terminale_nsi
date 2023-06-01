import time

with open("Les_Miserables.txt") as f:
    roman = f.read().replace('\n', ' ')


def recherche_naive(texte, motif):
    '''
    renvoie la liste des indices (éventuellement vide) des occurrences de
    de la chaîne motif dans la chaîne texte.
    '''
    indices = []
    i = 0
    while i <= len(texte) - len(motif):
        k = 0
        while k < len(motif) and texte[i+k] == motif[k]:
            k += 1
        if k == len(motif):
            indices.append(i)
        i += 1

    return indices

t0 = time.time()
motif = "La chandelle était sur la cheminée et ne donnait que peu de clarté."
print(recherche_naive(roman, motif))
print(time.time()-t0)


t0 = time.time()
motif = "yeux"
print(recherche_naive(roman, motif))
print(time.time()-t0)
      

pieces  = [1,2,5,10,20,50,100,200]

def rendu(somme_a_rendre):
    i =  len(pieces)    # on part de l'indice de la dernière pièce, la plus grande
    solution = []
    while i > 0:
        if pieces[i- 1] <= somme_a_rendre : # est-ce que la pièce peut-être rendue ?
            solution.append(pieces[i- 1])   # on garde la pièce dans la liste solution
            somme_a_rendre = somme_a_rendre - pieces[i- 1] # on met à jour la somme à rendre
        else :
            i -= 1   # la pièce était trop grosse, on recule dans la liste
    return solution
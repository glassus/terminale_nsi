pieces = [1, 2, 5, 10, 20, 50, 100, 200]

def rendu_monnaie(somme_due, somme_versee):
    '''Renvoie la liste des pièces à rendre pour rendre la monnaie
    lorsqu'on doit rendre somme_versee - somme_due'''
    rendu = ... 
    a_rendre = ... 
    i = len(pieces) - 1
    while a_rendre > ...: 
        while pieces[i] > a_rendre:
            i = i - 1
        rendu.append(...) 
        a_rendre = ... 
    return rendu



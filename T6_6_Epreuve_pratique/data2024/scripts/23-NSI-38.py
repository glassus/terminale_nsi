def est_cyclique(plan):
    '''
    Prend en paramètre un dictionnaire `plan` correspondant à un plan d'envoi de messages (ici entre les personnes A, B, C, D, E, F).
    Renvoie True si le plan d'envoi de messages est cyclique et False sinon.
    '''
    expediteur = 'A'
    destinataire = plan[...]
    nb_destinaires = 1
    
    while destinataire != ...:
        destinataire = plan[...]
        nb_destinaires += ...

    return nb_destinaires == ...

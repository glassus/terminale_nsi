def insere(a, tab):
	""" Insère l'élément a (int) dans le tableau tab (list)
        trié par ordre croissant à sa place et renvoie le
        nouveau tableau. """
    l = list(tab) #l contient les memes elements que tab
    l.append(a)
    i = ...
    while a < ... and i >= 0: 
      l[i+1] = ...
      l[i] = a
      i = ...
    return l

```python linenums='1'
from random import randint

def plus_ou_moins():
    nb_mystere = randint(1,100)
    nb_test = int(input('Proposez un nombre entre 1 et 99 : '))
    compteur = 0

    while nb_mystere != nb_test and compteur < 10 :
        compteur = compteur + 1
        if nb_mystere > nb_test:
            nb_test = int(input('Trop petit ! Testez encore : '))
        else:
            nb_test = int(input('Trop grand ! Testez encore : '))

    if nb_mystere == nb_test:
        print ('Bravo ! Le nombre était ', nb_mystere)
        print('Nombre d essais: ', compteur)
    else:
        print ('Perdu ! Le nombre était ', nb_mystere)

```
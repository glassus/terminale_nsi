{{initexo(0)}}

!!! example "{{ exercice() }}"
    Exercice 1 du [Asie J1 2025](https://glassus.github.io/terminale_nsi/T6_Annales/data/2025/25-NSIJ1JA1.pdf){. target="_blank"} 

    {{
    correction(True,
    """
    ??? success \"Correction Q1\" 
        ```x``` vaut 0 et ```y``` vaut 20.  
    """
    )
    }}

    {{
    correction(True,
    """
    ??? success \"Correction Q2\" 
        Un fichier Python est un fichier texte, on peut donc le percevoir comme une chaine de caractères.  
    """
    )
    }}

    {{
    correction(True,
    """
    ??? success \"Correction Q3\" 
        Les programmes 3 et 5 terminent.

        Les programmes 4 et 6 ne terminent pas.  
    """
    )
    }}

    {{
    correction(True,
    """
    ??? success \"Correction Q4\" 
        Ce programme ne répond pas au problème car si le programme ne s'arrête pas (à la ligne 2), le programme ne renverra jamais ```False```.   
    """
    )
    }}

    {{
    correction(True,
    """
    ??? success \"Correction Q5\" 
        L'algorithme de Boyer-Moore est un algorithme de recherche de texte qui utilise un dictionnaire pour faire des décalages intelligents et ainsi accélérer la recherche.  
    """
    )
    }}

    {{
    correction(True,
    """
    ??? success \"Correction Q6\" 
        ```python
        def arret_essai2(programme):
            return not recherche('while', programme)
        ```   
    """
    )
    }}

    {{
    correction(True,
    """
    ??? success \"Correction Q7\" 
        Avec le programme suivant :
        ```python
        def programme():
            print('boucle infinie !')
            programme()
        ```  
        ```arret_essai2(programme)``` renverra ```True``` alors que le programme ne s'arrête pas.  

        Avec le programme suivant :
        ```python
        def programme():
            n = 3
            while n > 0:
                print(n)
                n -= 1
        ```  
        ```arret_essai2(programme)``` renverra ```False``` alors que le programme s'arrête.  

    """
    )
    }}


    {{
    correction(True,
    """
    ??? success \"Correction Q8\" 
        ```python
        def terminaison_inverse(programme):
            if arret(programme) == True:
                boucle_infinie()
            else:
                print('stop')
        ```

    """
    )
    }}

    {{
    correction(False,
    """
    ??? success \"Correction Q9\" 
        Si ```programme_paradoxal``` termine, alors ```terminaison_inverse(programme_paradoxal)``` ne termine pas.

        Si ```programme_paradoxal``` ne termine pas, alors ```terminaison_inverse(programme_paradoxal)``` termine.     
    """
    )
    }}


    {{
    correction(False,
    """
    ??? success \"Correction Q10\" 
        La question 9. a abouti à une contradiction. Celle-ci est due à la non-existence de la fonction ```arret```.    
    """
    )
    }}


    {{
    correction(False,
    """
    ??? success \"Correction Q11\" 
        Cette impossibilité n'est pas due aux limitations du langage Python. Elle est générale, et a été démontrée en 1936 par Alan Turing sous le nom *Théorème de l'arrêt*.   
    """
    )
    }}
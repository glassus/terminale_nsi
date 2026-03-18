{{initexo(0)}}

!!! example "{{ exercice() }}"
    Exercice 1 du [Asie J1 2025](https://glassus.github.io/terminale_nsi/T6_Annales/data/2025/25-NSIJ1JA1.pdf){. target="_blank"}, questions 1 à 4. 

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
    correction(False,
    """
    ??? success \"Correction Q4\" 
        Ce programme ne répond pas au problème car si le programme ne s'arrête pas (à la ligne 2), le programme ne renverra jamais ```False```.   
    """
    )
    }}
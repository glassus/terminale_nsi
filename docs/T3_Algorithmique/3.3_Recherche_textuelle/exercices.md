{{initexo(0)}}

!!! example "{{ exercice() }}"
    Questions 14 et 15 de l'exercice 3 du [Sujet Métropole Septembre 2025](https://glassus.github.io/terminale_nsi/T6_Annales/data/2025/25-NSIJ1ME3.pdf){. target="_blank"}

    ```python linenums='1'
    def recherche_seq(seq, chaine):
        """Renvoie l'indice du premier caractère de
        chaine où commence `seq` si la séquence `seq`
        se trouve dans la chaine de caractères chaine,
        -1 sinon
        Paramètres:
        seq : séquence à rechercher
        chaine : chaine d'ADN
        Renvoie:
        indice du premier caractère de seq dans
        la chaine, -1 sinon.
        """
        for i in range(len(chaine)-len(seq) + 1):
            j = 0
            while j < len(seq) and ...:
                j += 1
            if ...:
                return i
        return -1
    ```

    {{
    correction(True,
    """
    ??? success \"Correction Q14.\" 
        ```python linenums='1'
        def recherche_seq(seq, chaine):
            '''Renvoie l'indice du premier caractère de
            chaine où commence `seq` si la séquence `seq`
            se trouve dans la chaine de caractères chaine,
            -1 sinon
            Paramètres:
            seq : séquence à rechercher
            chaine : chaine d'ADN
            Renvoie:
            indice du premier caractère de seq dans
            la chaine, -1 sinon.
            '''
            for i in range(len(chaine)-len(seq) + 1):
                j = 0
                while j < len(seq) and chaine[i+j] == seq[j]:
                    j += 1
                if j == len(seq):
                    return i
            return -1
        ```
    """
    )
    }}

    {{
    correction(True,
    """
    ??? success \"Correction Q15\" 
        Cet algorithme permet de faire des décalages intelligents si la lettre sur laquelle on est positionné fait partie ```seq```. Cela accélère considérablement la recherche par rapport à l'algorithme ```recherche_seq```. 
    """
    )
    }}
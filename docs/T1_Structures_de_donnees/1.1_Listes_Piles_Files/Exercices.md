
!!! example "{{ exercice() }}"
    === "Énoncé"
        Exercice 5 du sujet [Centres Étrangers 1 - 2021](https://glassus.github.io/terminale_nsi/T6_Annales/data/2021/21_Centres_Etrangers_1.pdf){. target="blank"}

    === "Correction Q1"
        ![image](data/ex1Q1.png){: .center width=50%}

    === "Correction Q2"
        ![image](data/ex1Q2.png){: .center width=50%}

<!--     === "Correction Q3"
        ```python linenums='1'
        def maximum(P):
            if est_vide(P):
                return None
            m = depile(P)
            while not est_vide(P):
                val = depile(P)
                if val > m:
                    m = val
            return m
        ```

        Avec le code ci-dessus, la pile ```p``` est vide à la fin de l'exécution. Pour éviter cela, on peut par exemple créer une pile ```q``` temporaire qui recevra les éléments de ```p```, avant de retransférer à la fin du programme les éléments de ```q```  dans ```p```.

        ```python linenums='1'
        def maximum(P):
            Q = creer_pile()
            if est_vide(P):
                return None
            m = depile(P)
            empile(Q, m)
            while not est_vide(P):
                val = depile(P)
                empile(Q, val)
                if val > m:
                    m = val
            while not est_vide(Q):
                empile(P, depile(Q))
            return m
        ```  -->

<!--     === "Correction Q4"
        **Q4a.** On va vider la pile ```p``` dans une pile ```q``` tout en comptant le nombre d'éléments dépilés dans une variable ```t```. 
        On redonne ensuite à ```p``` son état initial en vidant ```q``` dans ```p```.

        **Q4b**

        ```python linenums='1'
        def taille(P):
            if est_vide(P):
                return 0
            Q = creer_pile()
            t = 0
            while not est_vide(P):
                empile(Q, depile(P))
                t += 1
            while not est_vide(Q):
                empile(P, depile(Q))
            return t
        ``` -->
{{initexo(0)}}

!!! example "{{ exercice() }}"
    

    **Utilisation des bibliothèques cryptographiques du module ```sympy```.**


    Documentation : [https://docs.sympy.org/latest/modules/crypto.html](https://docs.sympy.org/latest/modules/crypto.html){target="_blank"}

    Décoder la phrase ```RYTVJKGCLJWRTZCVRMVTLEDFULCVHLZWRZKKFLKRMFKIVGCRTV```, sachant qu'elle a été chiffrée par décalage (*shift* en anglais...)

    {{
    correction(True,
    """
    ??? success \"Correction\" 
        ```python linenums='1'
        from sympy.crypto.crypto import decipher_shift

        msg = 'RYTVJKGCLJWRTZCVRMVTLEDFULCVHLZWRZKKFLKRMFKIVGCRTV'

        for cle in range(26):
            phrase = decipher_shift(msg, cle)
            print(phrase)
        ```        
    """
    )
    }}


!!! example "{{ exercice() }}"


    **Chiffrage affine**

    Principe du chiffrage affine :

    - Chaque lettre est codée par son rang, en commençant à 0 (A->0, B->1, ..., Z->25)
    - On applique à chaque rang la transformation affine 
    $f(x) = (ax+b)\, \%26$

    où $a$ et $b$ sont deux nombres entiers. Attention, $a$ doit être premier avec 26.

    !!! quote "Rappel sur les nombres premiers entre eux"
        Deux nombres sont dits *premiers entre eux* si leur PGCD vaut 1. 

        Exemples :
        
        - 8 et 15 sont premiers entre eux (ils n'ont aucun diviseur commun autre que 1)
        - 8 et 12 ne sont pas premiers entre eux (leur PGCD vaut 4).

    **Q1.** Codez votre fonction ```affine(msg, a, b)```.

    Pour tester votre fonction :
    ```python
    >>> affine("BONJOUR", 3, 5)
    'IVSGVNE'
    ```

    {{
    correction(True,
    """
    ??? success \"Correction\" 
        ```python linenums='1'
        def rang(lettre):
            return ord(lettre) - 65

        def affine(msg, a, b):
            sol = ''
            for lettre in msg:
                rg = rang(lettre)
                nv_rg = (a*rg + b) % 26 #chiffrement affine
                nv_lettre = chr(nv_rg + 65)
                sol += nv_lettre
            return sol
        ```        
    """
    )
    }}



    **Q2.** Comparez vos résultats avec ceux obtenus par la fonction ```encipher_affine()``` de ```sympy```.

    **Q3.** Décodez la phrase ```UCGXLODCMOXPMFMSRJCFQOGTCRSUSXC```, sachant qu'elle contient le mot ```TRAVAIL``` et que $a$ et $b$ sont inférieurs à 20.

    !!! tip "Aide"
        L'instruction ```gcd``` du module ```math``` permet de calculer le PGCD de deux nombres.

    {{
    correction(True,
    """
    ??? success \"Correction\" 
        ```python linenums='1'
        from sympy.crypto.crypto import decipher_affine
        from math import gcd

        for a in range(1,20):
            if gcd(a,26) == 1:
                for b in range(1,20):
                    p = decipher_affine('UCGXLODCMOXPMFMSRJCFQOGTCRSUSXC', (a, b))
                    if 'TRAVAIL' in p:
                        print(p)
        ```        
    """
    )
    }}



!!! example "{{ exercice() }}"
    Exercice 3 (Parties A et B) du sujet [Métropole J2 2025](https://glassus.github.io/terminale_nsi/T6_Annales/data/2025/25_NSIJ2ME1.pdf){. target="_blank"}

    **Partie A**

    ```python
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
    'W', 'X', 'Y', 'Z']
    ```

    {{
    correction(True,
    """
    ??? success \"Correction Q1\" 
        On obtient le mot PGRDX. 
    """
    )
    }}

    {{
    correction(True,
    """
    ??? success \"Correction Q2\" 
        ```python
        def indice(L, element):
            for i in range(len(L)):
                if L[i] == element:
                    return i  
        ```
    """
    )
    }}

    {{
    correction(True,
    """
    ??? success \"Correction Q3\" 
        ```python
        def lettres_vers_indices(txt):
            lst = []
            for c in txt:
                lst.append(indice(alphabet,c))
            return lst
        ```
    """
    )
    }}

    ```python
    def indices_vers_lettres(lst):
        s = ''
        for c in lst:
            s += alphabet[c]
        return s
    ```

    ```python
    def chiffrement(msg, cle):
        assert len(cle) >= len(msg), 'impossible'
        indices_msg = lettres_vers_indices(msg)
        indices_cle = lettres_vers_indices(cle)
        n = len(msg)
        indices_msg_chiffre = []
        for k in range(n):
            ind = ...
            if ind >= 26:
                ind = ...
            indices_msg_chiffre.append(ind)
        msg_chiffre = indices_vers_lettres(...)
        return msg_chiffre    
    ```

    {{
    correction(True,
    """
    ??? success \"Correction Q4\" 
        ```python
        def chiffrement(msg, cle):
            assert len(cle) >= len(msg), 'impossible'
            indices_msg = lettres_vers_indices(msg)
            indices_cle = lettres_vers_indices(cle)
            n = len(msg)
            indices_msg_chiffre = []
            for k in range(n):
                ind = indices_msg[k] + indices_cle[k]
                if ind >= 26:
                    ind = ind - 26
                indices_msg_chiffre.append(ind)
            msg_chiffre = indices_vers_lettres(indices_msg_chiffre)
            return msg_chiffre
        ```
    """
    )
    }}

    {{
    correction(True,
    """
    ??? success \"Correction Q5\" 
        On obtient AssertionError 'impossible' car la longueur de la clé est inférieure
        à la longueur du message. 
    """
    )
    }}

    {{
    correction(True,
    """
    ??? success \"Correction Q6\" 
        On obtient le mot BRAVO.
    """
    )
    }}

    {{
    correction(True,
    """
    ??? success \"Correction Q7\" 
        Pour chaque caractère du message chiffré, on effectue la soustraction entre sa position dans l’alphabet et la position du caractère associé dans le masque. Si la valeur obtenue est strictement négative, on ajoute 26. On obtient finalement la
        position du caractère en clair dans l’alphabet.
    """
    )
    }}

    {{
    correction(True,
    """
    ??? success \"Correction Q8\" 
        ```python
        def dechiffrement(msg, cle):
            assert len(cle) >= len(msg), 'impossible'
            indices_msg = lettres_vers_indices(msg)
            indices_cle = lettres_vers_indices(cle)
            n = len(msg)
            indices_msg_dechiffre = []
            for k in range(n):
                ind = indices_msg[k] - indices_cle[k]
                if ind < 0:
                    ind = ind + 26
            indices_msg_dechiffre.append(ind)
            msg_dechiffre = indices_vers_lettres(indices_msg_dechiffre)
            return msg_dechiffre
        ```
    """
    )
    }}


    **Partie B**

    {{
    correction(True,
    """
    ??? success \"Correction Q9\" 
        Avec un chiffrement symétrique, la connaissance d'une seule et unique clé est requise pour chiffrer et déchiffrer le message. Dans un chiffrement asymétrique, la clé de déchiffrement est connue seulement du destinataire, alors que la clé de chiffrement est publique et distribuée à tous.
    """
    )
    }}

    {{
    correction(True,
    """
    ??? success \"Correction Q10\" 
        Il suffit à Bob de déchiffer le message avec sa clé privée.
    """
    )
    }}

    {{
    correction(True,
    """
    ??? success \"Correction Q11\" 
        Tout le monde a la clé publique de Bob, donc tout le monde peut écrire en se faisant passer pour Alice.
    """
    )
    }}

    {{
    correction(True,
    """
    ??? success \"Correction Q12\" 
        Dans le protocole ```https```, une clé AES est générée par chiffrement asymétrique au tout début de la communication (TLS). Ensuite, le reste du flux est chiffré avec le chiffrement symétrique AES.
    """
    )
    }}

    {{
    correction(True,
    """
    ??? success \"Correction Q13\" 
        Utiliser un chiffrement asymétrique tout au long de la navigation ralentirait considérablement le trafic car un chiffrement asymétrique consomme beaucoup de ressources de calcul, contrairement au chiffrement symétrique.
    """
    )
    }}






!!! example "{{ exercice() }}"
    **Cryptographie RSA** presque à la main



    ```python linenums='1'
    import Crypto
    import libnum
    from Crypto.Util.number import bytes_to_long, long_to_bytes
    from Crypto.Random import get_random_bytes 

    bits = 256

    p = ...
    q = ...

    n = ...
    phi = ...

    e = 65537  # très souvent choisi comme exposant de chiffrement
    d = ...  # on calcule l'inverse de e modulo phi


    def encipher(msg):
        M = bytes_to_long(msg.encode('utf-8')) # on convertit le message msg en un nombre M
        c = ... # M puissance e modulo n
        return c

    def decipher(c):
        res = ...
        return long_to_bytes(res) # on convertit le nombre res en une chaine de caractères


    ```

    - Pour générer un grand nombre premier de taille ```bits``` , on utilise la fonction ```Crypto.Util.number.getPrime(bits, randfunc=get_random_bytes)```.
    - Pour inverser un nombre $x$ modulo $n$, on utilise la fonction    ```pow(x, -1, n)```.
    - Pour calculer ```a``` à la puissance ```b``` modulo ```n```, on utilise ```pow(a, b, n)```.

    {{
    correction(True,
    """
    ??? success \"Correction\" 
        ```python linenums='1'
        import Crypto
        from Crypto.Util.number import bytes_to_long, long_to_bytes
        from Crypto.Random import get_random_bytes 

        bits = 256

        p = Crypto.Util.number.getPrime(bits, randfunc=get_random_bytes)
        q = Crypto.Util.number.getPrime(bits, randfunc=get_random_bytes)

        n = p * q
        phi = (p - 1) * (q - 1)

        e = 65537  # 65537 est un nombre qui sera (normalement) premier avec phi
        d = pow(e, -1, phi)  # on calcule l'inverse de e modulo phi


        def encipher(msg):
            M = bytes_to_long(msg.encode('utf-8'))
            c = pow(M, e, n) # M puissance e modulo n
            return c

        def decipher(c):
            res = pow(c, d, n)
            return long_to_bytes(res)



        ```        
    """
    )
    }}


!!! example "{{ exercice() }}"

    En vous servant du code précédent, déchiffrez le message ```58152918114477529438769495136495430966050302170947748011925859233600631318929939319619808279389222131229963717435870597641010567365311762267359794338657867540621133550787677728203831932548041236152866441194127191404729294628415184239755221703677388875259927092794165578604353985011899152968982365630138088486380827379488939561996226754182```  sachant que :

    - $e$ vaut 65537.
    - $p$ et $q$ sont respectivement les 13èmes et 14èmes nombres de Mersenne.

    {{
    correction(True,
    """
    ??? success \"Correction\" 
        ```python linenums='1'
        import Crypto
        from Crypto.Util.number import bytes_to_long, long_to_bytes
        from Crypto.Random import get_random_bytes 


        p = 2**521 - 1 # 13ème nombre de Mersenne
        q = 2**607 - 1 # 14ème nombre de Mersenne


        n = p * q
        phi = (p - 1) * (q - 1)

        e = 65537  # 65537 est un nombre premier, donc forcément premier avec phi
        d = pow(e, -1, phi)  # on calcule l'inverse de e modulo phi

        c = 58152918114477529438769495136495430966050302170947748011925859233600631318929939319619808279389222131229963717435870597641010567365311762267359794338657867540621133550787677728203831932548041236152866441194127191404729294628415184239755221703677388875259927092794165578604353985011899152968982365630138088486380827379488939561996226754182

        def decipher(c):
            res = pow(c, d, n)
            return long_to_bytes(res)
        ```        
    """
    )
    }}



!!! example "{{ exercice() }}"
    **module RSA** dans les règles de l'art



    ```python
    from Crypto.PublicKey import RSA
    from Crypto.Cipher import PKCS1_OAEP
    import binascii

    keyPair = RSA.generate(1024)

    pubKey = keyPair.publickey()

    pubKeyPEM = pubKey.exportKey()

    privKeyPEM = keyPair.exportKey()


    msg = b'vive la crypto en NSI !'
    encryptor = PKCS1_OAEP.new(pubKey)
    encrypted = encryptor.encrypt(msg)
    print("Encrypted:", binascii.hexlify(encrypted))


    decryptor = PKCS1_OAEP.new(keyPair)
    decrypted = decryptor.decrypt(encrypted)
    print('Decrypted:', decrypted)
    ```

!!! example "{{ exercice() }} <i id="ex3J1PO2025"></i>"
    Exercice 3 du sujet [Polynésie J1 2025](https://glassus.github.io/terminale_nsi/T6_Annales/data/2025/25-NSIJ1PO1.pdf){. target="_blank"}

    ```python linenums='1'
    from random import randint

    def gen_mdp(longueur, cont_min, cont_maj, cont_spe):
        # Pour qu'un mot de passe soit non vide, il doit
        # pouvoir contenir des minuscules ou des majuscules
        # ou des caractères spéciaux.
        assert (cont_min or cont_maj or cont_spe)
        minuscules = [chr(i) for i in ...]
        majuscules = [...]
        caracteres_speciaux = ... + ...
        jeu_caracteres = []
        if cont_min:
            ...
        ...
            ...
        ...
            ...
        mot_de_passe = ''
        n = len(jeu_caracteres)
        for i in range(longueur):
            mot_de_passe = ...
        return mot_de_passe
    ```

    {{
    correction(True,
    """
    ??? success \"Correction Q1\"
        ```python
        gen_mdp(8, True, True, False)
        ``` 
        
    """
    )
    }}

    {{
    correction(True,
    """
    ??? success \"Correction Q2\"
        ```python linenums='8'
        minuscules = [chr(i) for i in range(97, 123)]
        majuscules = [chr(i) for i in range(65, 91)]
        caracteres_speciaux = [chr(i) for i in range(33, 48)] + [chr(i) for i in range(58, 65)]
        ```
        
    """
    )
    }}

    {{
    correction(True,
    """
    ??? success \"Correction Q3\"
        ```python linenums='12'
        if cont_min:
            jeu_caracteres += minuscules
        if cont_maj:
            jeu_caracteres += majuscules
        if cont_spe:
            jeu_caracteres += caracteres_speciaux
        ```
        
    """
    )
    }}

    {{
    correction(True,
    """
    ??? success \"Correction Q4\"
        ```python linenums='1'
        from random import randint

        def gen_mdp(longueur, cont_min, cont_maj, cont_spe):
            # Pour qu'un mot de passe soit non vide, il doit
            # pouvoir contenir des minuscules ou des majuscules
            # ou des caractères spéciaux.
            assert (cont_min or cont_maj or cont_spe)
            minuscules = [chr(i) for i in range(97, 123)]
            majuscules = [chr(i) for i in range(65, 91)]
            caracteres_speciaux = [chr(i) for i in range(33, 48)] + [chr(i) for i in range(58, 65)]
            jeu_caracteres = []
            if cont_min:
                jeu_caracteres += minuscules
            if cont_maj:
                jeu_caracteres += majuscules
            if cont_spe:
                jeu_caracteres += caracteres_speciaux
            mot_de_passe = ''
            n = len(jeu_caracteres)
            for i in range(longueur):
                mot_de_passe = mot_de_passe + jeu_caracteres[randint(0, n-1)]
            return mot_de_passe

        ```
        
    """
    )
    }}

    {{
    correction(True,
    """
    ??? success \"Correction Q5\"
        Comme on utilise une fonction aléatoire, rien ne garantit qu'on aura un caractère spécial ou une lettre minuscule.
        
    """
    )
    }}
    

    {{
    correction(True,
    """
    ??? success \"Correction Q6\"
        Le principe d'une clé primaire est de référence de manière unique chaque enregistrement. Si l'attribut ```mot_de_passe``` est déclaré clé primaire de la table ```compte```, il est alors impossible d'avoir le même mot de passe pour deux sites différents.
        
    """
    )
    }}

    {{
    correction(True,
    """
    ??? success \"Correction Q7\"
        ```sql
        SELECT url
        FROM site
        ```
        
    """
    )
    }}

    {{
    correction(True,
    """
    ??? success \"Correction Q8\"
        ```sql
        UPDATE compte
        SET mot_de_passe = '@rDfohpj!&'
        WHERE mot_de_passe = 'yhTS?d@UTJe'
        ```
        
    """
    )
    }}

    {{
    correction(True,
    """
    ??? success \"Correction Q9\"
        ```sql
        SELECT id_site
        FROM compte
        WHERE renouvellement < '2024-03-20'
        ```
        
    """
    )
    }}

    {{
    correction(True,
    """
    ??? success \"Correction Q10\"
        Ce format de date permet de faire des comparaisons entre les dates, puisqu'on commence par l'année, puis le mois, puis le jour. 
        
        Avec le format JJ-MM-AAAA, le fait de commencer par le jour rend la date '01-02-2023' inférieure à la date '13-06-2022', ce qui est illogique.
        
    """
    )
    }}

    {{
    correction(True,
    """
    ??? success \"Correction Q11\"
        ```sql
        SELECT compte.mot_de_passe, compte.utilisateur
        FROM compte
        JOIN site ON site.id = compte.id_site
        WHERE site.nom_site = 'Votremailp'
        ORDER BY compte.renouvellement
        ```
        
    """
    )
    }}

    {{
    correction(True,
    """
    ??? success \"Correction Q12\"
        Utiliser deux tables permet à Alice de ne pas mélanger les informations : une table pour la gestion de ses mots de passe, une page pour les sites.
        
    """
    )
    }}

    {{
    correction(True,
    """
    ??? success \"Correction Q13\"
        ```chiffrement('gestionnaire.db', '../Perso/secret.db', '../Perso/cle')``` 
        
    """
    )
    }}

    {{
    correction(True,
    """
    ??? success \"Correction Q14\"
        
        - ```A3``` correspond au nombre décimal 163, donc au nombre binaire ```10100011```.  
        - ```59``` correspond au nombre décimal 89, donc au nombre binaire ```1011001```.
        - L'opération XOR entre les nombres binaires ```10100011``` et ```1011001``` donne 250, qui s'écrit ```FA``` en hexadécimal.
    """
    )
    }}



    {{
    correction(True,
    """
    ??? success \"Correction Q15\"
        |`a`| `b` | `a XOR b`|`(a XOR b) XOR b`|
        |:--:|:-:|:--:|:--:|
        |0|0|0|0|
        |1|0|1|1|
        |0|1|1|0|
        |1|1|0|1|

        La colonne ```(a XOR b) XOR b``` est identique la colonne ```a```.  
    """
    )
    }}

    {{
    correction(True,
    """
    ??? success \"Correction Q16\"
        L'opération XOR permet de chiffrer et de déchiffrer avec la même clé, ce qui est caractéristique d'un chiffrement symétrique.        
    """
    )
    }}

    {{
    correction(True,
    """
    ??? success \"Correction Q17\"
        Le fichier ```secret.db``` étant directement accessible en lecture pour tout le monde, il est donc à la merci d'un attaquant. Alice devrait restreindre les droits en lecture de son fichier pour ne le rendre lisible que par elle-même.       
    """
    )
    }}

    {{
    correction(True,
    """
    ??? success \"Correction Q18\"

        - Alice a des mots de passe différents pour chaque site, elle respecte donc la recommandation P1.
        - Ses mots de passe sont bien de longueur minimale 8 et contiennent des minuscules, des majuscules, des chiffres et des caractères spéciaux. Elle respecte donc la recommandation P2.
        - On ne sait pas si Alice communique ou non ses mots de passe à des tiers. On ne peut donc rien dire sur la recommandation P3.
        - Alice n'utilise pas de gestionnaire de mots de passe : elle ne respecte donc pas la recommandation P4.
    """
    )
    }}

!!! example "{{ exercice() }} <i id="ex3J2ME2025"></i>"
    Exercice 3 du sujet [Métropole J2 2025](https://glassus.github.io/terminale_nsi/T6_Annales/data/2025/25_NSIJ2ME1.pdf){. target="_blank"}

    {{
    correction(False,
    """
    ??? success \"Correction Q1\" 
        Prenons comme exemple la deuxième lettre, I. Son rang est 8. La lettre du masque qui lui correspond est Y, qui est de rang 24.

        $8+24=32=6\%26$

        On prend donc la lettre de rang 6, qui est G.

        Si on fait de même pour les autres lettres, on trouve PGRDX.
    """
    )
    }}

    {{
    correction(False,
    """
    ??? success \"Correction Q2\" 
        ```python
        def indice(L, element):
            for i in range(len(L)):
                if L[i] == element:
                    return i
        ```
    """
    )
    }}
    
    {{
    correction(False,
    """
    ??? success \"Correction Q3\" 
        ```python
        def lettres_vers_indices(chaine):
            lst = []
            for car in chaine:
                lst.append(indice(alphabet, car))
            return lst
        ```
    """
    )
    }}

    ```python
    def indices_vers_lettres(lst):
        s = ''
        for k in lst:
            s += chr(65+k)
        return s

    def chiffrement(msg, cle):
        assert len(cle) >= len(msg), 'impossible'
        indices_msg = lettres_vers_indices(msg)
        indices_cle = lettres_vers_indices(cle)
        n = len(msg)
        indices_msg_chiffre = []
        for k in range(n):
            ind = ...
            if ind >= 26:
                ind = ...
            indices_msg_chiffre.append(ind)
        msg_chiffre = indic
        return msg_chiffre
    ```

    {{
    correction(False,
    """
    ??? success \"Correction Q4\" 
        ```python
        def chiffrement(msg, cle):
            assert len(cle) >= len(msg), 'impossible'
            indices_msg = lettres_vers_indices(msg)
            indices_cle = lettres_vers_indices(cle)
            n = len(msg)
            indices_msg_chiffre = []
            for k in range(n):
                ind = indices_msg[k] + indices_cle[k]
                if ind >= 26:
                    ind = ind % 26
                indices_msg_chiffre.append(ind)
            msg_chiffre = indices_vers_lettres(indices_msg_chiffre)
            return msg_chiffre
        ```
    """
    )
    }}

    {{
    correction(False,
    """
    ??? success \"Correction Q5\" 
        La longueur de la clé est plus petite que le message à chiffrer, donc la fonction va s'arrêter au premier ```assert``` et renvoyer ```impossible```.
    """
    )
    }}

    {{
    correction(False,
    """
    ??? success \"Correction Q6\" 
        On obtient le message ```BRAVO```.
    """
    )
    }}

    {{
    correction(False,
    """
    ??? success \"Correction Q7\" 
        Prenons par exemple l'avant-dernière lettre du message chiffré, D. Elle a été chiffrée avec la lettre I.

        D a pour rang 3, I a pour rang 8. On fait 3 - 8, qui donne -5. On ajoute 26 pour finalement trouver 21. La lettre de rang 21 est la lettre V.
    """
    )
    }}

    {{
    correction(False,
    """
    ??? success \"Correction Q8\" 
        ```python
        def dechiffrement(msg, cle):
            assert len(cle) >= len(msg), 'impossible'
            indices_msg = lettres_vers_indices(msg)
            indices_cle = lettres_vers_indices(cle)
            n = len(msg)
            indices_msg_chiffre = []
            for k in range(n):
                ind = indices_msg[k] - indices_cle[k]
                if ind < 0:
                    ind = ind + 26
                indices_msg_chiffre.append(ind)
            msg_chiffre = indices_vers_lettres(indices_msg_chiffre)
            return msg_chiffre

        ```
    """
    )
    }}


    {{
    correction(False,
    """
    ??? success \"Correction Q9\" 
        Dans un chiffrement symétrique, c'est la même clé qui sert à chiffrer et à déchiffrer.

        Dans un chiffrement asymétrique, il y a 2 clés, une clé publique et une clé privée.
        Si Bob veut communiquer avec Alice, il va chiffrer son message avec la clé publique d'Alice. Seule Alice pourra le déchiffrer à l'aide de sa clé privée. 
    """
    )
    }}

    {{
    correction(False,
    """
    ??? success \"Correction Q10\" 
        Il suffit à Bob d'appliquer sa clé privée sur le message envoyé par Alice. 
    """
    )
    }}

    {{
    correction(False,
    """
    ??? success \"Correction Q11\" 
        Comme tout le monde connaît la clé publique de Bob, rien ne garantit qu'Alice est l'expéditrice du message.
    """
    )
    }}

    {{
    correction(False,
    """
    ??? success \"Correction Q12\" 
        Le protocole HTTPS fonctionne en 2 temps.

        Dans un premier temps, le client et le serveur vont échanger une clé en utilisant un chiffrement asymétrique (souvent RSA).

        Dans un second temps, ils vont communiquer en chiffrement symétrique (souvent AES) avec la clé échangée au préalable.
    """
    )
    }}

    {{
    correction(False,
    """
    ??? success \"Correction Q13\" 
        Le chiffrement asymétrique demande beaucoup de ressources, il n'est donc pas adapté aux échanges rapides. 
    """
    )
    }}

    {{
    correction(False,
    """
    ??? success \"Correction Q14\" 
        Marc s'est trompé dans le troisième octet de l'adresse IP. Il aurait dû écrire ```ping 192.168.110.115```. 
    """
    )
    }}

    {{
    correction(False,
    """
    ??? success \"Correction Q15\" 
        Le masque en binaire ```11111111.11111111.11111111.11100000``` a pour représentation décimale ```255.255.255.224```. (on convertit chaque octet en décimal) 
    """
    )
    }}

    {{
    correction(False,
    """
    ??? success \"Correction Q16\" 
        Il y a 5 bits à zéro dans le masque, ce qui donne 32 adresses disponibles. Si on enlève la première (adresse du réseau) et la dernière (adresse de broadcast), il reste 30 adresses disponibles.
    """
    )
    }}

    {{
    correction(False,
    """
    ??? success \"Correction Q17\" 
        134 s'écrit ```10000110``` en binaire.
    """
    )
    }}

    {{
    correction(False,
    """
    ??? success \"Correction Q18\" 
        L'adresse IP ```192.168.110.134``` donne une adresse de réseau de ```192.168.110.128```.

        L'adresse IP ```192.168.110.115``` (commande n°1) donne une adresse de réseau de ```192.168.110.32```.

        L'adresse IP ```192.168.110.153``` (commande n°2) donne une adresse de réseau de ```192.168.110.128```.

        Seule le ping de la commande n°2 peut donc aboutir.
    """
    )
    }}

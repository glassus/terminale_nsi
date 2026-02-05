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
    correction(False,
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
    correction(False,
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

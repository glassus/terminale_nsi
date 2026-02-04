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
    correction(False,
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
    correction(False,
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

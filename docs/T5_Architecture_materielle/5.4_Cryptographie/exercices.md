{{initexo(0)}}

!!! abstract "{{ exercice() }}"

    **Utilisation des bibliothèques cryptographiques du module ```sympy```.**


    Documentation : [https://docs.sympy.org/latest/modules/crypto.html](https://docs.sympy.org/latest/modules/crypto.html){target="_blank"}

    Décoder la phrase ```RYTVJKGCLJWRTZCVRMVTLEDFULCVHLZWRZKKFLKRMFKIVGCRTV```, sachant qu'elle a été chiffrée par décalage (*shift* en anglais...)

    {{
    correction(False,
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


!!! abstract "{{ exercice() }}"


    **Chiffrage affine**

    Principe du chiffrage affine :

    - Chaque lettre est codée par son rang, en commençant à 0 (A->0, B->1, ..., Z->25)
    - On applique à chaque rang la transformation affine 
    $f(x) = (ax+b)\, \%26$

    où $a$ et $b$ sont deux nombres entiers. Attention, *a* doit être premier avec 26.

    !!! quote "Rappel sur les nombres premiers entre eux"
        Deux nombres sont dits *premiers entre eux* si leur PGCD vaut 1. 

        Exemples :
        
        - 8 et 15 sont premiers entre eux (ils n'ont aucun diviseur commun autre que 1)
        - 8 et 12 ne sont pas premiers entre eux (leur PGCD vaut 4).

    **Q1.** Codez votre fonction ```affine(msg, a, b)```

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
            for b in range(1,20):
                if gcd(a,26) == 1:
                    p = decipher_affine('UCGXLODCMOXPMFMSRJCFQOGTCRSUSXC', (a,b))
                    if 'TRAVAIL' in p:
                        print(p)
        ```        
    """
    )
    }}





!!! abstract "{{ exercice() }}"
    **Cryptographie RSA** presque à la main



    ```python linenums='1'
    import Crypto
    import libnum
    from Crypto.Util.number import bytes_to_long, long_to_bytes
    from Crypto.Random import get_random_bytes 

    bits = 256
    msg = "en NSI on fait de la crypto"

    p = Crypto.Util.number.getPrime(bits, randfunc=get_random_bytes)
    q = Crypto.Util.number.getPrime(bits, randfunc=get_random_bytes)

    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537  # 65537 est un nombre premier, donc forcément premier avec phi
    d = libnum.invmod(e, phi)  # on calcule l'inverse de e modulo phi

    M = bytes_to_long(msg.encode('utf-8'))

    c = pow(M, e, n) # M puissance e modulo n
    res = pow(c, d, n)

    print(long_to_bytes(res))


    ```

    1. Analysez le programme ci-dessous pour y retrouver chaque étape du chiffrement RSA.
    2. Exécutez le programme et regardez en console le contenu des différentes variables.
    3. Observez les deux lignes qui contiennent les opérations de chiffrement et de déchiffrement : que faut-il changer pour chiffrer avec la clé privée et déchiffrer avec la clé publique ?

    {{
    correction(False,
    """
    ??? success \"Correction\" 
        Q3. Il suffit d'inverser ```e``` et ```d```  dans les lignes 20 et 21.  
    """
    )
    }}


!!! abstract "{{ exercice() }}"

    En vous servant du code précédent, déchiffrez le message ```58152918114477529438769495136495430966050302170947748011925859233600631318929939319619808279389222131229963717435870597641010567365311762267359794338657867540621133550787677728203831932548041236152866441194127191404729294628415184239755221703677388875259927092794165578604353985011899152968982365630138088486380827379488939561996226754182```  sachant que :

    - $e$ vaut 65537.
    - $p$ et $q$ sont respectivement les 13èmes et 14èmes nombres de Mersenne.

    {{
    correction(False,
    """
    ??? success \"Correction\" 
        ```python linenums='1'
        import Crypto
        import libnum
        from Crypto.Util.number import bytes_to_long, long_to_bytes
        from Crypto.Random import get_random_bytes 


        p = 2**521 - 1
        q = 2**607 - 1


        n = p * q
        phi = (p - 1) * (q - 1)

        e = 65537  # 65537 est un nombre premier, donc forcément premier avec phi
        d = libnum.invmod(e, phi)  # on calcule l'inverse de e modulo phi

        c = 58152918114477529438769495136495430966050302170947748011925859233600631318929939319619808279389222131229963717435870597641010567365311762267359794338657867540621133550787677728203831932548041236152866441194127191404729294628415184239755221703677388875259927092794165578604353985011899152968982365630138088486380827379488939561996226754182

        res = pow(c, d, n)

        print(long_to_bytes(res))
        ```        
    """
    )
    }}



!!! abstract "{{ exercice() }}"
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

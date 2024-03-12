On considère des mots à trous : ce sont des chaînes de caractères contenant uniquement
des majuscules et des caractères `*`. Par exemple `INFO*MA*IQUE`, `***I***E**` et
`*S*` sont des mots à trous.  

Programmer une fonction `correspond` qui :

- prend en paramètres deux chaînes de caractères `mot` et `mot_a_trous` où
`mot_a_trous` est un mot à trous comme indiqué ci-dessus, 
- renvoie :
    - `True` si on peut obtenir `mot` en remplaçant convenablement les caractères
`'*'` de `mot_a_trous`.
    - `False` sinon.


Exemple :

```python
>>> correspond('INFORMATIQUE', 'INFO*MA*IQUE')
True
>>> correspond('AUTOMATIQUE', 'INFO*MA*IQUE')
False
>>> correspond('STOP', 'S*')
False
>>> correspond('AUTO', '*UT*')
True
```
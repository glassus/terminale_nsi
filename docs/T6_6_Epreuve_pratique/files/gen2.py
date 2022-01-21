import os
import sys

NB_DOSS = 40

lst = ['{:02d}'.format(k) for k in range(1, NB_DOSS+1)]

def create_doss():
    for nom in lst:
        os.makedirs(nom + '_1', exist_ok = True)
        os.makedirs(nom + '_2', exist_ok = True)

def fichier(nom_doss):
    nom_file = nom_doss + '/' + 'enonce.md'
    with open(nom_file, 'w') as f:
        f.write("")
        
    nom_file = nom_doss + '/' + 'correction.md'
    with open(nom_file, 'w') as f:
        f.write("")

def fichiers_1_2():
    for nom_doss in lst:
        n1 = nom_doss + '_1'
        n2 = nom_doss + '_2'
        fichier(n1)
        fichier(n2)


create_doss()
fichiers_1_2()




contenu = """
### Exercice {0}.1 □
!!! example "Exercice {0}.1"
    === "Énoncé" 
        --8<-- "docs/T6_6_Epreuve_pratique/files/{0}_1/enonce.md"

    === "Correction"
        --8<-- "docs/T6_6_Epreuve_pratique/files/{0}_1/correction.md"

    === "Source Markdown"
            --8<-- "docs/T6_6_Epreuve_pratique/files/{0}_1/enonce.md"


### Exercice {0}.2 □
!!! example "Exercice {0}.2"
    === "Énoncé" 
        --8<-- "docs/T6_6_Epreuve_pratique/files/{0}_2/enonce.md"

    === "Correction"
        --8<-- "docs/T6_6_Epreuve_pratique/files/{0}_2/correction.md"

    === "Sources Markdown"
        ```md
        --8<-- "docs/T6_6_Epreuve_pratique/files/{0}_2/enonce.md"
        ```             
        """


with open('BNS_2022.md', 'w') as f:
    for val in lst:
        f.write(contenu.format(val))




# nom_dossier = 'listes_logins'
# nom_sources = "sources"
# os.makedirs(nom_dossier, exist_ok = True)
# os.makedirs(nom_sources, exist_ok = True)
# for file in os.scandir(nom_dossier):
#     os.remove(file.path)
# 
# 
# 
# 
# for classe in classes:
#     print(classe)
#     nomhtml = nom_sources + '/' + classe + '.html'
#     with open(nomhtml, 'w') as f:
#         f.write(html_start)
#         f.write('<h1> ' + classe + ' - logins Scribe </h1>')
#         f.write(tabdf[classe].to_html(index=False))
#         f.write(html_end)
#     nom_fichier = nom_dossier + '/' + classe + '.pdf'
#     pdf.from_file(nomhtml, nom_fichier)
#     os.remove(nomhtml)
# os.rmdir(nom_sources)
# print("Terminé")
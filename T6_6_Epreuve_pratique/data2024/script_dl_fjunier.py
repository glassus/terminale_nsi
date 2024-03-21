#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:41:10 2024

@author: fjunier
"""

import json
import os
import requests

r = requests.get(
    "https://cyclades.education.gouv.fr/delos/api/public/sujets/ece?sort=libelle&clef=%22NSI%22&order=ASC&page=0&itemsPerPage=200"
)
with open("NSI.json", mode="w") as f:
    f.write(r.text)

with open("NSI.json") as f:
    data = f.read()
    dico = json.loads(data)

for k, sujet in enumerate(dico["content"], 1):
    num = "{:02d}".format(k)
    os.mkdir(num)
    for (i, fichier) in enumerate(sujet["fichiers"]):
        r = requests.get(
            f"https://cyclades.education.gouv.fr/delos/api/file/public/{fichier['id']}"
        )
        if "%PDF" in r.text:
            chemin_disque = num + '/24-NSI-' + num + '.pdf'
            mode_ecriture = "wb"
        else:
            chemin_disque = num + '/24-NSI-' + num + '.py'
            mode_ecriture = "w"
        with open(chemin_disque, mode=mode_ecriture) as g:
            if mode_ecriture == "w":
                g.write(r.text)
            else:
                g.write(r.content)
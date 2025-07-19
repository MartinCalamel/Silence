"""
# Auteur : Wallaby
# Date : 2025-07-18
# Objet :
# TODO : test unitaires
"""

import modules.info as info
import csv


def exist_file(file_name: str) -> bool:
    """
    # exist_file
    ## Fonction
    retourne si un fichoier existe ou non
    ## Input
    * file_name : str -> Nom du fichier + path si requis
    ## Output
    Bool
    """
    try:
        f = open(file_name)
        f.close()
        return True
    except FileNotFoundError:
        info.error("Fichier non trouvé")
        return False


def read(file_name: str, delimiter: str) -> list:
    """
    # read
    ## Fonction
    lit un fichier s'il exite et retourne son contenu sous
    la forme [lignes[delimiteur]]
    ## Input
    * file_name : str -> Nom du fichier + path si requis
    * delimiter : str -> Symbole qui sépare les éléments d'une même ligne
    ## Outputresult = file.read()
    liste des lignes et des éléments
    """
    data: list = []
    if exist_file(file_name):
        with open(file_name, "r") as file:
            content = csv.reader(file, delimiter)
            for ligne in content:
                data.append(ligne)
    return data


def write(file_name: str, data: str) -> None:
    """
    # write
    ## Fonction
    ecrit le contenue de data dans le fichier en EFFACANT
    le contenue du fichier
    ## Input
    * file_name : str -> Nom du fichier + path si requis
    * data : str -> Contenue à ecrire dans le fichier
    ## Output
    None
    """
    with open(file_name, "w") as file:
        file.write(data)
    return None


def add(file_name: str, data: str) -> None:
    """
    # add
    ## Fonction
    Ajoute le contenue de data au fichier s'il exite
    on créé une nouvelle ligne
    ## Input
    * file_name : str -> Nom du fichier + path si requis
    * data : str -> Contenue à ajouter dans le fichier
    ## Output
    None
    """
    if exist_file(file_name):
        with open(file_name, "a") as file:
            file.write("\n")
            file.write(data)
    return None

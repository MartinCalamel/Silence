"""
# Auteur : Wallaby
# Date : 2025-09-10
# Objet : fonction pour le protocole d'authentification
# TODO :    fonction d'enregistrement d'user
            Fonction de verrification d'utilisateur
            couverture de test
"""

import modules.files as files
import modules.hash as hash
import modules.type as type
import modules.info as info

# Nom du fichier où sont enregistré les mots de passes et les nom d'utilisateur 
PASSWORD_USERNAME_FILENAME: str = "/temp/passwd.txt"


def is_username_used(username: str) -> bool:
    """
    # is username_used
    ## Fonction
    On verrifie dans le fichier des mots de passes
    et noms d'utilisateur que le nom d'utilisateur n'y est pas.
    ## Input
    * username: str -> Nom d'utilisateur à controler
    ## Output
    * bool -> est ce que l'utilisateur est dans le fichier
    """

    # Verification des types (test des paramètres)
    type.check_type(username, str)

    data: list = files.read(PASSWORD_USERNAME_FILENAME, ";")
    list_username: list = [ligne[0] for ligne in data]

    if username in list_username:
        info.error("Nom d'utilisateur déjà utilisé")
        return False
    return True


def get_user_log_info(username: str) -> list:
    """
    # get_user_log_info
    ## Fonction
    Permet de réccuperer les informations de sel et mot de passe
    d'un utilisateur.
    ## Input
    * username: str -> Nom de l'utilisateur
    ## Output
    result: list -> resultat
    """
    data: list = files.read(PASSWORD_USERNAME_FILENAME, ";")
    info_user = [user for user in data if user[0] == username]

    if not len(info_user) == 1:
        info.error("L'utilisateur n'existe pas ou existe en double!")
        return []
    return info_user[0]


def new_user(username: str, password: str) -> bool:
    """
    # new_user
    ## Fonction
    Gestion d'un nouvel utilisateur
    ## Input
    * username: str -> Nom de l'utilisateur
    * password: str -> Mot de passe de l'utilisateur
    ## Output
    * valid: bool -> authentification validée
    """

    # Verification des types (test des paramètres)
    type.check_type(username, str)
    type.check_type(password, str)

    if not files.exist_file(PASSWORD_USERNAME_FILENAME):
        files.create_file(PASSWORD_USERNAME_FILENAME, "")
    else :
        if is_username_used(username):
            return False
    
    hashed_password: str = hash.make_hash(password)
    data: str = username + ";" + hashed_password

    files.add(PASSWORD_USERNAME_FILENAME, data)
    
    return True

def verif_user(username: str, password: str) -> bool:
    """
    # verif_user
    ## Fonction
    Lit le fichier des utilisateurs et verifie que le mot de passe
    est bien associé au nom d'utilisateur.
    ## Input
    * username: str -> Nom de l'utilisateur
    * password: str -> Mot de passe de l'utilisateur
    ## Output
    * valid: bool -> authentification validée
    """

    # Verification des types (test des paramètres)
    type.check_type(username, str)
    type.check_type(password, str)

    if not files.exist_file(PASSWORD_USERNAME_FILENAME):
        info.error("Le fichier contenant les mots de passe " \
        "et les utilisateur n'existe pas.\n verifier le chemin d'accès")
        return False
    
    info_user = get_user_log_info(username)
    if info_user == []:
        return False
    
    return hash.check_hash(password, ";".join(info_user[1:])) 
    


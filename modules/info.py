"""
# Auteur : Wallaby
# Date : 2025-07-18
# Objet :
# TODO :
"""
from colorama import Fore, init
from modules.type import check_type

init()


def error(message: str) -> None:
    """
    # error
    ## Fonction
    Affiche un message d'erreur en rouge
    ## Input
    * message : str -> message à afficher
    ## Output
    None
    """

    # Verification des types (test des paramètres)
    check_type(message, str)

    print(Fore.RED, "\nError : ", message, Fore.WHITE)

"""
# Auteur : Wallaby
# Date : 2025-07-18
# Objet :
# TODO :
"""
from colorama import Fore, init

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
    print(Fore.RED, "\nError : ", message, Fore.WHITE)

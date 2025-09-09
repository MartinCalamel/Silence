"""
# Auteur : Wallaby
# Date : 2025-09-09
# Objet : gestion des type et verrification du bon format de ceux ci
# TODO :    fonction de verification
            gestion des erreurs
"""

from modules.info import error
import sys


def check_type(var: any, type_cible: any) -> bool:
    """
    # check_type
    ## Fonction
    Verifie que le type de la variable est bien celui attendu.  
    Dans le cas contraire, génère une erreur.
    ## Input
    * var: any -> variable dont on veux verifier le type
    * type_cible: any -> type dont doit être la variable
    ## Output
    * result: bool -> Resultat de la verification
    """
    if isinstance(var, type_cible):
        return True
    error("le type de la variable n'est pas le bon")
    sys.exit()

"""
# Auteur : Wallaby
# Date : 2025-09-05
# Objet : Module pour la gestion et la validation
            des hash avec integration du sel
# TODO :    - comparaison de hash
            - gestion du sel
            - validation de hash
            - génération de hash
"""

import hashlib
import random
import string

from modules.type import check_type

ALPHA = string.ascii_letters + string.digits


def make_salt(len: int) -> bytes:
    """
    # make_salt
    ## Fonction
    Générer un sel (chaîne de charactère aléatoire) pour le hash
    ## Input
    * len: int -> taille du sel
    ## Output
    * sel: int -> sel aléatoire
    """

    # Verification des types (test des paramètres)
    check_type(len, int)

    sel = ''.join(random.choice(ALPHA) for _ in range(len))
    return sel


def make_hash(text: str) -> str:
    """
    # make_hash
    ## Fonction
    Générer un hash à partir d'une chaîne de charactère
    ## Input
    * text: str -> chaîne de charactère à transformer en hash
    ## Output
    result: str -> sel+hash au format {sel;hash}
    """

    # Verification des types (test des paramètres)
    check_type(text, str)

    sel: bytes = make_salt(20).encode("utf-8")
    encoded_text: bytes = text.encode("utf-8")
    hash: bytes = hashlib.pbkdf2_hmac("sha256", encoded_text, sel, 100000)
    hash = hash.hex()
    result: str = sel.decode("utf-8") + ";" + hash
    return result


def check_hash(text: str, hash_and_salt: str) -> bool:
    """
    #check_hash
    ## Fonction
    Comparer un text avec un hash.
    ## Input
    * text: str -> chaîne à comparer
    * hash_and_salt: str -> sel et hash à comparer format {sel;hash}
    ## Output
    * result: bool -> est-ce-que le text est bon
    """

    # Verification des types (test des paramètres)
    check_type(text, str)
    check_type(hash_and_salt, str)

    sel, hash = hash_and_salt.split(";")
    sel = sel.encode("utf-8")
    hash = hash.encode("utf-8")
    encoded_text = text.encode("utf-8")
    result = hashlib.pbkdf2_hmac("sha256", encoded_text, sel, 100000).hex()
    return result == hash.decode("utf-8")

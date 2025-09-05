import pytest

from modules.hash import make_hash, make_salt, check_hash

def test_hash():
    text = "password"
    text2 = "not_password"

    # test de la fonction de génération de hash et de validation

    hash_and_salt = make_hash(text)
    assert check_hash(text, hash_and_salt)
    assert not check_hash(text2, hash_and_salt)


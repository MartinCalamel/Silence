import pytest

from modules.auth_protocol import *

user1 = "bob"
user2 = "dad"
user3 = "lou"
pass1 = "password"
pass2 = "not_password"


def test_auth():

    assert new_user(user1, pass1)
    assert new_user(user2, pass2)
    assert not new_user(user1, pass2)

    assert verif_user(user1, pass1)
    assert not verif_user(user2, pass1)
    assert not verif_user(user3, pass1)

import pytest


from modules.files import read, write, add, exist_file


def test_files():
    file = "tests/test_file.txt"
    assert exist_file(file)
    assert not exist_file("non_exist.txt")

    assert read(file, ";") == [["data", "test"]]

    add(file, "bonjour;salut")
    assert read(file, ";") == [["data", "test"], ["bonjour", "salut"]]

    write(file, "data;test")
    assert read(file, ';') == [["data", "test"]]

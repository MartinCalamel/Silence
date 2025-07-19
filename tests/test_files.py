import pytest
from modules.files import read, write, add, exist_file

def test_files():
    file = "tests/test_file.txt"
    assert exist_file(file) == True
    assert exist_file("non_exist.txt") == False

    assert read(file,";") == [["data", "test"]]
    
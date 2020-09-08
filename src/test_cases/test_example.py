from src.main.example import hi, bye, how_are_you
import pytest

@pytest.fixture
def bob():
    return {"name":"Naresh"}
def test_hi(bob):
    #bob = {"name": "Naresh"}
    assert hi(bob) == "Hi, Naresh"


def test_bye(bob):
    #bob = {"name": "Naresh"}
    assert bye(bob) == "Bye, Naresh"


def test_how_are_you(bob):
    #bob = {"name": "Naresh"}
    assert how_are_you(bob) == "How are you, Naresh"

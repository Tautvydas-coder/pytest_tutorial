import pytest


@pytest.mark.sanity
def testLogin():
    print("Login successful")


def testLogoff():
    print("Logoff successful")


def testCalculation():
    assert 2 + 2 == 4
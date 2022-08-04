import pytest


@pytest.fixture(scope="session", autouse=True)
# autouse=True all procees will be run
def tc_setup(browser):
    if browser == "chrome":
        print("Launch chrome")
    elif browser == "ff":
        print("Launch firefox")
    else:
        print("provide valid browser")
    print("Login")
    print("Browse products")
    yield
    print("Logoff")
    print("Close Browser")


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="session", autouse=True)
def browser(request):
    return request.config.getoption("--browser")

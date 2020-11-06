from pytest import fixture
from config import Config
import json
from selenium import webdriver

#************************************
# Reffer: https://docs.pytest.org/en/stable/fixture.html
# Fixtures are created when first requested by a test, and are destroyed based on their scope:
#       function: the default scope, the fixture is destroyed at the end of the test.
#       class: the fixture is destroyed during teardown of the last test in the class.
#       module: the fixture is destroyed during teardown of the last test in the module.
#       package: the fixture is destroyed during teardown of the last test in the package.
#       session: the fixture is destroyed at the end of the test session.
#************************************

def pytest_addoption(parser):
    parser.addoption(
        "--env", 
        action="store",
        help="Environment to run test case. this is custom message"    
    )


@fixture(scope="session")
def env_fixture(request):
    return request.config.getoption("--env")


@fixture(scope="session")
def app_config_fixture(env_fixture):
    cfg = Config(env_fixture)
    return cfg


@fixture(scope='function')
def chrome_browser():
    browser = webdriver.Chrome()
    return browser

@fixture(
    scope='session', 
    params=[webdriver.Chrome, webdriver.Edge]
    )
def browser(request):
    driver = request.param
    drvr = driver()
    yield drvr
    drvr.quit()


def load_test_data(path):
    with open(path) as data_file:
        data = json.load(data_file)
        return data


@fixture(params=load_test_data("test_data.json"))
def tv_brand(request):
    data = request.param
    return data

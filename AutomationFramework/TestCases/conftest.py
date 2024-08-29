import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="class")
def tc_setup(browser,request):
    if browser == "chrome":
        print("Chrome Browser Was Launched")
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)

    elif browser == "firefox":
        print("Firefox was Launched")
        driver = webdriver.Firefox()

    elif browser == "edge":
        print("Edge was Launched")
        driver = webdriver.edge()
    else:
        print("enter valid browser")

    driver.maximize_window()
    driver.get("https://aeuat.benekiva.io/login")
    request.cls.driver = driver

    yield
    print("close browser")
    driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="browser option: chrome or ff"
    )

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from Utilities.readConfig import ReadConfig

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="function")
def setup(request):
    browser = request.config.getoption("--browser")
    
    if browser == "Chrome":
        print("Running in Chrome")
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless")  # Uncomment for headless mode (Jenkins)
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
    elif browser == "Edge":
        print("Running in Edge")
        options = webdriver.EdgeOptions()
        # options.add_argument("--headless")  # Uncomment for headless mode (Jenkins)
        driver = webdriver.Edge(
            service=EdgeService(EdgeChromiumDriverManager().install()),
            options=options
        )
    else:
        print("Running in Chrome (default)")
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )

    driver.maximize_window()
    driver.get(ReadConfig.get_baseurl())

    yield driver
    driver.quit()

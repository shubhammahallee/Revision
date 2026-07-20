import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Utilities.readConfig import ReadConfig

def pytest_addoption(parser):
    parser.addoption("--browser", default="Chrome")

@pytest.fixture(scope="function")
def setup(request):
    browser = request.config.getoption("--browser")
    
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    
    driver.maximize_window()
    driver.get(ReadConfig.get_baseurl())
    
    yield driver
    driver.quit()

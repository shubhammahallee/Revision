import pytest
import undetected_chromedriver as uc
from Utilities.readConfig import ReadConfig

def pytest_addoption(parser):
    parser.addoption("--browser", default="Chrome")

@pytest.fixture(scope="function")
def setup(request):
    browser = request.config.getoption("--browser")
    
    options = uc.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    
    driver = uc.Chrome(options=options, version_main=None)
    
    driver.maximize_window()
    driver.get(ReadConfig.get_baseurl())
    
    yield driver
    driver.quit()

import pytest
from selenium import webdriver
import data


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        data.DRIVER_NAME = 'chrome'
        driver = webdriver.Chrome()
    else:
        data.DRIVER_NAME = 'firefox'
        driver = webdriver.Firefox()
    yield driver
    driver.quit()

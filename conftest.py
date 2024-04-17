from selenium import webdriver
import pytest


@pytest.fixture(scope="class")
def setup(request):
        driver=webdriver.Chrome()
        driver.get("https://demowebshop.tricentis.com/")
        driver.maximize_window()
        request.cls.driver = driver
        yield driver
        driver.quit()

        
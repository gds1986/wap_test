import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()

    # Emulate mobile device
    mobile_emulation = {
        "deviceMetrics": {"width": 375, "height": 750, "pixelRatio": 3.0},
        "userAgent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/131.0.6778.260 Mobile Safari/537.36",
    }
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

    # Create a new instance of the Chrome browser
    # using local chromedriver
    service = Service('/usr/bin/chromedriver')
    driver = webdriver.Chrome(service=service, options=chrome_options)

    yield driver
    driver.quit()
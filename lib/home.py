from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self._url = "https://m.twitch.tv/"
        self._browse = (By.LINK_TEXT, "Browse")
        self.load()

    def load(self):
        self.driver.get(self._url)

        # Remove cookie consent banner, could not accept or reject due to a glitch
        self.driver.execute_script("""
            var element = document.querySelector(".consent-banner");
            if (element)
                element.parentNode.removeChild(element);
            """)

    def click_search(self):
        self.driver.find_element(*self._browse).click()

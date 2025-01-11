import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BrowsePage:

    def __init__(self, driver):
        self.driver = driver
        self._search_box = (By.XPATH, "//input[@type='search']")
        self._tablist = (By.XPATH, "//ul[@role='tablist']")
        self._body = (By.TAG_NAME, 'body')
        self._videos = (By.XPATH, "//button[contains(@class, 'tw-link')]")
        self._start_watching_button = (By.XPATH, "//button[@data-a-target='content-classification-gate-overlay-start-watching-button']")
        self._channel_overlay = (By.ID, "channel-live-overlay")

    def search(self, value):
        search_box = WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(self._search_box))
        search_box.send_keys(value)
        search_box.send_keys(Keys.RETURN)
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(self._tablist))

    def scroll_down(self):
        self.driver.find_element(*self._body).send_keys(Keys.PAGE_DOWN)
        time.sleep(1)

    def select_streamer(self):
        videos = self.driver.find_elements(*self._videos)
        for video in videos:
            if video.is_displayed():
                self.driver.execute_script("arguments[0].click();", video)

                # Handle Modal/pop-up to start watching if present
                try:
                    WebDriverWait(self.driver, 3).until(
                        ec.visibility_of_element_located(self._start_watching_button)).click()
                except TimeoutException:
                    print("no modal or pop-up")

                    # Wait till page is loaded
                    WebDriverWait(self.driver, 3).until(
                        ec.visibility_of_element_located(self._channel_overlay))
                    break

    def take_screenshot(self):
        self.driver.save_screenshot("screenshot.png")
from lib.home import HomePage
from lib.browse import BrowsePage


def test_search_twitch(driver):

    # Open twitch webpage with the emulated device
    home_page = HomePage(driver)

    # Click on search
    home_page.click_search()

    # Input value
    browse_page = BrowsePage(driver)
    browse_page.search("StarCraft II")

    # Scroll down 2 times
    browse_page.scroll_down()
    browse_page.scroll_down()

    # Select one streamer
    browse_page.select_streamer()

    # Take screenshot
    browse_page.take_screenshot()



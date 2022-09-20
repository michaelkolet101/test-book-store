from playwright.sync_api import sync_playwright


class Base_page:
    def __init__(self, driver: sync_playwright):
        self._driver = driver
        super().__init__(self._driver)

    def find_element(self, token: str):
        elem = self._driver.wait_for_selector(token)
        return elem

    def find_elements(self, token: str):
        elements = self._driver.query_selector_all(token)
        return elements



from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import EXPLICIT_WAIT

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, EXPLICIT_WAIT)

    def wait_for_clickable_element(self, locator):
        """显式等待：等待元素可点击（通用方法）"""
        return self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f"元素 {locator} 在超时时间内不可点击"
        )

    def wait_for_visible_element(self, locator):
        """等待元素可见"""
        return self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f"元素 {locator} 在超时时间内不可见"
        )

    def find_element(self, locator):
        """查找元素（带等待）"""
        return self.wait_for_visible_element(locator)

    def click_element(self, locator):
        """点击元素"""
        self.wait_for_clickable_element(locator).click()
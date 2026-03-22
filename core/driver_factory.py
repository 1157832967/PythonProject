from appium import webdriver
from config.capabilities import get_platform_caps
from config.settings import APPIUM_SERVER_URL

class DriverFactory:
    _driver = None

    @classmethod
    def create_driver(cls):
        """创建并返回单例 driver"""
        if not cls._driver:
            caps = get_platform_caps()
            cls._driver = webdriver.Remote(APPIUM_SERVER_URL, caps)
        return cls._driver

    @classmethod
    def quit_driver(cls):
        """销毁驱动"""
        if cls._driver:
            cls._driver.quit()
            cls._driver = None
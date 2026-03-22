from appium.webdriver.common.appiumby import AppiumBy
from core.base_page import BasePage
from config.settings import PLATFORM_NAME

class LoginPage(BasePage):
    # 跨平台定位器
    if PLATFORM_NAME == "android":
        USERNAME_INPUT = (AppiumBy.ID, "com.vis.mobility:id/username")
        LOGIN_BUTTON = (AppiumBy.ID, "com.vis.mobility:id/login_btn")
    else:
        USERNAME_INPUT = (AppiumBy.IOS_PREDICATE, 'label == "Username"')
        LOGIN_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Login")

    def enter_username(self, text: str):
        """输入用户名"""
        username_field = self.find_element(self.USERNAME_INPUT)
        username_field.clear()
        username_field.send_keys(text)

    def tap_login_button(self):
        """点击登录按钮"""
        self.click_element(self.LOGIN_BUTTON)
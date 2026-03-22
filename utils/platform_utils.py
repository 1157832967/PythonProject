from appium.webdriver.common.appiumby import AppiumBy
from config.settings import PLATFORM_NAME

class PlatformUtils:
    @staticmethod
    def get_submit_button_locator():
        """
        动态获取 Submit 按钮定位器
        Android: UIAutomator
        iOS: Accessibility ID / Predicate
        """
        if PLATFORM_NAME.lower() == "android":
            return (AppiumBy.ANDROID_UIAUTOMATOR, 'text("Submit")')
        elif PLATFORM_NAME.lower() == "ios":
            return (AppiumBy.ACCESSIBILITY_ID, "Submit")
        else:
            raise ValueError("不支持的平台")
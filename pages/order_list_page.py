from appium.webdriver.common.appiumby import AppiumBy
from core.base_page import BasePage
from utils.element_utils import extract_order_number

class OrderListPage(BasePage):
    # 订单标题定位器
    ORDER_TITLE = (AppiumBy.XPATH, "//*[contains(@text, 'Order #') or contains(@label, 'Order #')]")

    def wait_for_any_order(self):
        """等待任意订单出现"""
        return self.wait_for_visible_element(self.ORDER_TITLE)

    def get_first_visible_order_full_text(self):
        """获取第一个可见订单完整文本"""
        self.wait_for_any_order()
        return self.find_element(self.ORDER_TITLE).text

    def get_first_order_number(self):
        """获取第一个订单的纯数字编号"""
        full_text = self.get_first_visible_order_full_text()
        return extract_order_number(full_text)
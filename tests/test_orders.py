from pages.order_list_page import OrderListPage

def test_get_first_order_number(appium_driver):
    order_page = OrderListPage(appium_driver)
    order_num = order_page.get_first_order_number()
    print(f"提取到的第一个订单号: {order_num}")
    assert order_num.isdigit()
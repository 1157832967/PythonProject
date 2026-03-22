from pages.login_page import LoginPage

def test_login(appium_driver):
    login_page = LoginPage(appium_driver)
    login_page.enter_username("test_user")
    login_page.tap_login_button()
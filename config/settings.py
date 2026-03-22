from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions

# 全局显式等待时间（秒）
IMPLICIT_WAIT = 5
EXPLICIT_WAIT = 15

# Appium 服务地址
APPIUM_SERVER_URL = "http://127.0.0.1:4723"

# 平台类型：android / ios
PLATFORM_NAME = "android"

# 日志配置
LOG_PATH = "./logs/automation.log"

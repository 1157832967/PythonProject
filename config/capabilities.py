from config.settings import PLATFORM_NAME

def get_android_capabilities():
    """Android 设备配置"""
    caps = {
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "deviceName": "Android Emulator",
        "appPackage": "com.vis.mobility",
        "appActivity": "com.vis.mobility.MainActivity",
        "noReset": True,
        "newCommandTimeout": 60
    }
    return caps

def get_ios_capabilities():
    """iOS 设备配置"""
    caps = {
        "platformName": "iOS",
        "automationName": "XCUITest",
        "deviceName": "iPhone Simulator",
        "bundleId": "com.vis.mobility",
        "noReset": True,
        "newCommandTimeout": 60
    }
    return caps

def get_platform_caps():
    """根据配置自动获取对应平台能力"""
    if PLATFORM_NAME.lower() == "android":
        return get_android_capabilities()
    elif PLATFORM_NAME.lower() == "ios":
        return get_ios_capabilities()
    else:
        raise ValueError("仅支持 Android / iOS 平台")
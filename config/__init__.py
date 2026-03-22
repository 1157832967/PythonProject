# 配置包初始化
__version__ = "1.0.0"
__author__ = "VIS-MOBILITY Automation Team"

# 导出核心配置，方便外部导入
from .settings import (
    IMPLICIT_WAIT,
    EXPLICIT_WAIT,
    APPIUM_SERVER_URL,
    PLATFORM_NAME
)
from .capabilities import get_platform_caps, get_android_capabilities, get_ios_capabilities
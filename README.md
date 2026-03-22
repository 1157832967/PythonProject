1a:macOS Android Appium 环境完整搭建步骤
1 安装 Homebrew
2 安装 Node.js + Appium：brew install node && npm install -g appium
3 安装 UiAutomator2 驱动：appium driver install uiautomator2
4 安装 Android SDK 并配置环境变量（ANDROID_HOME）
5 创建 Android 模拟器并启动
6 验证：adb devices、appium 启动服务

1b:iOS 真机 vs 模拟器 关键区别
1 模拟器：无需苹果开发者账号，自动安装 WDA
2 真机：必须付费开发者账号 + Xcode 签名 + 手动安装 WDA + 设备授权
3 定位：iOS 用 accessibility id / predicate，比 Xpath 更稳定

2a:iOS 嵌套层级定位策略
1 优先使用：ACCESSIBILITY_ID / IOS_PREDICATE
2 示例：(AppiumBy.IOS_PREDICATE, 'type == "XCUIElementTypeCollectionView" AND label CONTAINS "Order"')

2b:订单提取
在目录utils/element_utils.py和pages/order_list_pages.py
等待 → 取文本 → 正则提取纯数字

2c:find_element 失败原因 & 解决方案
1 元素存在但不可见 / 不可点击
2 视图滚动、元素被遮挡
3 嵌套 WebView / 弹窗遮挡
4 解决：显式等待 + 等待可点击 + 滚动到元素 + 安全点击

3:pytest fixture
在目录tests/conftest.py里面实现了session级别的appium_driver

4a/4b:
在 base_page.py 和login_page.py实现了oom page

5:
在 utils/platform_utils.py里面实现了跨平台的submit


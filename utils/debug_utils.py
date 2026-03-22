from loguru import logger
from appium.webdriver.common.touch_action import TouchAction

def safe_click(driver, element):
    """
    安全点击方法：处理 Android content-desc 含换行符等异常
    1. 原生点击
    2. 失败 → 打印元素属性
    3. 降级 → TouchAction 点击
    """
    try:
        element.click()
        logger.info("原生点击成功")
    except Exception as e:
        # 失败日志：输出关键属性
        logger.error(f"原生点击失败: {str(e)}")
        try:
            attr_text = element.get_attribute("text")
            attr_desc = element.get_attribute("contentDescription")
            logger.error(f"元素文本: {attr_text}")
            logger.error(f"元素描述: {attr_desc}")

            # 降级方案：TouchAction 点击
            action = TouchAction(driver)
            action.tap(element).perform()
            logger.info("降级 TouchAction 点击成功")
        except Exception as fallback_e:
            logger.critical(f"所有点击方案均失败: {str(fallback_e)}")
            raise
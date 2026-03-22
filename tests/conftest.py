import pytest
from loguru import logger
import sys
from core.driver_factory import DriverFactory
from config.settings import LOG_PATH, EXPLICIT_WAIT

# ======================
# 日志全局配置
# ======================
logger.remove()  # 移除默认日志
logger.add(
    sys.stdout,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | <cyan>{message}</cyan>",
    level="INFO"
)

# 输出日志到文件
logger.add(
    LOG_PATH,
    rotation="10 MB",
    retention=7,
    encoding="utf-8",
    level="DEBUG"
)

# ======================
# 核心 fixture：appium_driver
# 题目 3a 强制要求：session 级别
# ======================
@pytest.fixture(scope="session", autouse=False)
def appium_driver():
    """
    整个测试会话只启动一次 driver
    所有测试用例共享同一个 session
    测试全部结束后自动退出
    """
    driver = None

    try:
        logger.info("=" * 60)
        logger.info("🚀 开始初始化 Appium Driver (session 级别)")
        logger.info("=" * 60)
        # 创建驱动
        driver = DriverFactory.create_driver

        # 设置隐式等待
        driver.implicitly_wait(IMPLICIT_WAIT)

        # 把 driver 抛给测试用例
        yield driver

    except Exception as e:
        logger.critical(f"❌ Driver 启动失败: {str(e)}")
        raise

    finally:
        # 所有测试跑完 → 自动退出 driver
        if driver:
            logger.info("=" * 60)
            logger.info("🛑 所有测试完成，关闭 Appium Driver")
            logger.info("=" * 60)
            DriverFactory.quit_driver()


# ======================
# 可选：自动给所有测试用例带上 driver（不需要可删除）
# ======================
def pytest_runtest_setup(item):
    """测试用例前置钩子"""
    logger.info(f"\n🔹 开始执行测试: {item.name}")
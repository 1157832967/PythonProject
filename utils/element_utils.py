import re
from loguru import logger

def extract_order_number(order_text: str) -> str:
    """
    从 'Order #12345' 提取纯数字订单号
    返回：12345
    """
    match = re.search(r"Order #(\d+)", order_text)
    if match:
        return match.group(1)
    logger.warning(f"无法从文本提取订单号: {order_text}")
    return ""
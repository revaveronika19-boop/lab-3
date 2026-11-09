"""Математичні та предметні операції."""
from ..errors import RuleError

def safe_divide(a: float, b: float) -> float:
    """Ділить два числа.

    Args:
        a (float): чисельник.
        b (float): знаменник.
    Returns:
        float: частка.
    Raises:
        ZeroDivisionError: нульовий знаменник.
    """
    return a / b

def process_value(value: int) -> int:
    """Перевіряє невід'ємність числа.

    Args:
        value (int): вхідне значення.
    Returns:
        int: перевірене значення.
    Raises:
        RuleError: від'ємне значення.
    """
    try:
        if value < 0: raise RuleError('невід’ємне число')
        return value
    except RuleError:
        print('Журнал: помилкове значення')
        raise

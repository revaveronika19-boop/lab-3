"""Розбір вхідних даних."""
import json
from ..errors import ValidationError, ResourceError

def parse_number(raw: str) -> int:
    """Перетворює рядок у число.

    Args:
        raw (str): вхідний рядок.
    Returns:
        int: ціле число.
    Raises:
        ValidationError: якщо число некоректне.
    """
    try: return int(raw)
    except (ValueError, TypeError) as exc: raise ValidationError('число') from exc

def load_json(path: str) -> dict:
    """Читає JSON через контекстний менеджер.

    Args:
        path (str): шлях до файлу.
    Returns:
        dict: вміст JSON.
    Raises:
        ResourceError: помилка читання файлу.
    """
    try:
        with open(path, encoding='utf-8') as f: return json.load(f)
    except (OSError, json.JSONDecodeError) as exc: raise ResourceError(path) from exc

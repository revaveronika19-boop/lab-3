"""Демонстрація сценаріїв помилок та пакету."""
import json
from app.errors import AppError, ValidationError, ResourceError, RuleError
from app.services.parser import parse_number, load_json
from app.services.operations import safe_divide, process_value

def main():
    print('1. try/except:')
    for raw in ['12', 'bad']:
        try: print(raw, parse_number(raw))
        except ValidationError as exc: print('Помилка:', exc)
    print('2. try/except/else/finally:')
    for pair in [(10,2), (10,0)]:
        try: result = safe_divide(*pair)
        except ZeroDivisionError: print('Помилка: ділення на нуль')
        else: print('Результат:', result)
        finally: print('finally: завершено спробу')
    print('3. Кілька типів:')
    for x in ['7', None]:
        try: print(int(x) + 1)
        except (TypeError, ValueError) as exc: print(type(exc).__name__)
    print('4. Власні виключення та cause:')
    for name in ['missing_file_12345.json']:
        try: load_json(name)
        except ResourceError as exc: print(str(exc), 'Причина:', type(exc.__cause__).__name__)
    try: process_value(-5)
    except AppError as exc: print('Базове виключення:', exc)
    print('5. Інтроспекція:', parse_number.__name__, parse_number.__annotations__)
    print('Doc:', parse_number.__doc__.splitlines()[0])
    print('Експорт пакету:', __import__('app').__all__)
if __name__ == '__main__': main()

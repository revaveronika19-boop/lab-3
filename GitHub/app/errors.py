"""Ієрархія прикладних виключень."""
class AppError(Exception):
    """Базова помилка застосунку."""
class ValidationError(AppError):
    def __init__(self, field): self.field = field
    def __str__(self): return f"Некоректне поле: {self.field}"
class ResourceError(AppError):
    def __init__(self, resource): self.resource = resource
    def __str__(self): return f"Ресурс недоступний: {self.resource}"
class RuleError(AppError):
    def __init__(self, rule): self.rule = rule
    def __str__(self): return f"Порушено правило: {self.rule}"

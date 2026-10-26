from functools import wraps

def my_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Вызов функции: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@my_logger
def calculate(a, b):
    """Складывает два числа."""
    return a + b

# Проверка:
print(calculate.__name__)
print(calculate.__doc__)
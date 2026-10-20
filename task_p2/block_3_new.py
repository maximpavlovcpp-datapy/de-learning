#1
from functools import wraps

def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Вызов функции {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_call
def multiply(a, b):
    """Умножает два числа."""
    return a * b

#print("Имя функции:", multiply.__name__)
#print("Документация:", multiply.__doc__)
#print("Результат:", multiply(3, 4))
#2
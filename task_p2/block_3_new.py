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
from functools import wraps

def repeat(num_times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result=None
            for _ in range(num_times):
                result=func(*args, **kwargs)
            return result
        return wrapper
    return decorator
    pass

@repeat(num_times=3)
def greet(name):
    print(f"Привет, {name}!")
    return "ok"

res = greet("Алексей")
print("Результат:", res)
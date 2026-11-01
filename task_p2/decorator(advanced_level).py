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
#print(calculate.__name__)
#print(calculate.__doc__)

#decorator with arg

from functools import wraps

def repeat(num_times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(num_times=3)
def greet(name):
    print(f"Привет, {name}!")

greet("Алексей")
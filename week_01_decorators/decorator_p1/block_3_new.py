#1.@wraps
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
#2.num_times
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
#print("Результат:", res)
#3.Timer
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time=time.perf_counter()
        res=func(*args, **kwargs)
        end_time=time.perf_counter()
        dif_time=end_time-start_time
        print(f"Функция {func.__name__} выполнилась за {dif_time:.4f} сек")
        return res
    return wrapper

@timer
def slow_task():
    """Имитирует долгую задачу."""
    time.sleep(0.1)
    return "готово"

res = slow_task()
print("Результат:", res)
import time
from functools import wraps

def rate_limit(max_calls, period):
    def decorator(func):
        # Храним историю вызовов в замыкании
        timestamps = []
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()
            
            # Очищаем метки, которые вышли за пределы временного окна:
            while timestamps and timestamps[0] < now - period:
                timestamps.pop(0)
            
            # Проверяем, не превышен ли лимит вызовов:
            if len(timestamps) >= max_calls:
                raise RuntimeError("Rate limit exceeded")
            
            # Добавляем текущее время в список:
            timestamps.append(now)
            
            return func(*args, **kwargs)
            
        return wrapper
    return decorator

# Тестовая функция
@rate_limit(max_calls=2, period=1.0)
def login(username):
    return f"Пользователь {username} успешно вошел"

# Проверка:
print(login("alex"))  # 1-й вызов - ок
print(login("alex"))  # 2-й вызов - ок
print(login("alex"))  # 3-й вызов без паузы - должен упасть с RuntimeError!

time.sleep(1.1)
print(login("alex"))  # После паузы - снова ок
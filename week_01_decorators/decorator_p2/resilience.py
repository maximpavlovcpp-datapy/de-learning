import time
from functools import wraps

def retry(max_attempts, delay=0.1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    # Пробуем выполнить функцию и сразу вернуть результат
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Попытка {attempt} провалилась: {e}")
                    if attempt == max_attempts:
                        # Попытки закончились, пробрасываем ошибку дальше
                        raise e
                    # Ждём перед следующей попыткой
                    time.sleep(delay)
        return wrapper
    return decorator

# Тестовая функция: падает первые 2 раза, на 3-й срабатывает
attempts_count = 0

@retry(max_attempts=2, delay=0.2)
def unstable_network_request():
    global attempts_count
    attempts_count += 1
    if attempts_count < 3:
        raise ConnectionError("Сетевой сбой (timeout)")
    return "200 OK: Данные получены"

# Проверка:
print(unstable_network_request())
def task1():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 22, 33]
    words = ["apple", "Banana", "cherry", "Date", "Elderberry"]
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    squares=[n**2 for n in numbers if n%2==0]
    print(squares)
    long_lower=[n.lower() for n in words if len(n)>5]
    print(long_lower)
    word_lengths={word: len(word) for word in words}
    print(word_lengths)
    initials={n[0] for n in words}
    print(initials)
    flat=[n for row in matrix for n in row]
    print(flat)
def example2_1():
    def cont_up(n):
        i=0
        while i<n:
            yield i
            i+=1
    for x in cont_up(5):
        print(x)    
def example2_2():
    squares=[n**2 for n in range(1000000)]
    print(squares)
#squares = (n ** 2 for n in range(1000000))   # ничего не посчитано
#for x in squares:                            # считает по одному
#    ...
def task_2_1():
    logs = [
    "INFO: server started",
    "ERROR: db connection failed",
    "INFO: retry",
    "ERROR: timeout",
    ]
    def read_log_lines(logs):
        for line in logs:
            if line .startswith("ERROR"):
                yield line
    for line in read_log_lines(logs):
        print(line)
def task_2_2():
    def fibonacci(n):
        a, b= 0, 1
        for _ in range(n):
            yield a
            a, b = b, a + b
    print(list(fibonacci(8)))                     
def task_2_3():
    def chunked(items, size):
        for i in range(0, len(items), size):
            yield items[i:i+size]
    print(list(chunked([1,2,3,4,5,6,7], 3)))
def task_2_4():
    def infinite_counter():
        start=0
        while True:
            yield start
            start+=1
    gen=infinite_counter()
    for n in range(9):
        print(next(gen))
# === Упражнение 1: Декоратор без @ ===

# 1. Это наша оригинальная функция
def say_hello(name):
    """Функция приветствия"""
    print(f"Привет, {name}!")

# 2. Это наш декоратор (пока просто обертка)
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("--- Начало работы ---")
        func(*args, **kwargs)       # Вызываем оригинал
        print("--- Конец работы ---")
    return wrapper

# 3. А теперь ВРУЧНУЮ применяем декоратор:
# Мы передаем функцию say_hello внутрь my_decorator
# и перезаписываем имя say_hello результатом
say_hello = my_decorator(say_hello)

# 4. Вызываем
say_hello("Максим")
#example 2: decotator with @
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("--- Начало работы ---")
        func(*args, **kwargs)       # Вызываем оригинал
        print("--- Конец работы ---")
    return wrapper
# magic with @
@my_decorator
def say_hello(name):    
    """Функция приветствия"""
    print(f"Привет, {name}!")   
#call 
say_hello("Максим")
# === Задача 3.1: Декоратор log_call===
def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"call: {func.__name__}")
        result=func(*args, **kwargs)
        print("ready!")
        return result
    return wrapper
@log_call
def add(a, b):
    return a + b
print(add(2, 3))






    

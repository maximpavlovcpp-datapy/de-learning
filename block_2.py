# === Задача 6.1 ===
cpu_load = 87
memory_load = 92

cpu_status = "HIGH" if cpu_load > 80 else "OK"
memory_status = "HIGH" if memory_load > 80 else "OK"

system_status = "CRITICAL" if cpu_status == "HIGH" or memory_status == "HIGH" else "NORMAL"

print(f"CPU: {cpu_status}")
print(f"Memory: {memory_status}")
print(f"System: {system_status}")
#==== Задача 7.1 =====
password = input("Введите пароль: ")

has_digit = any(c.isdigit() for c in password)
has_upper = any(c.isupper() for c in password)

if len(password) < 8:
    result = "Слабый: слишком короткий"
elif "password" in password.lower() or "123456" in password:
    result = "Слабый: очевидный пароль"
elif 8 <= len(password) <= 11 and has_digit:
    result = "Средний"
elif len(password) >= 12 and has_digit and has_upper:
    result = "Сильный"
else:
    result = "Средний"

print(f"Результат: {result}")
#==Task 7.2==
user_role= "admin"
is_active= True
ip_address="192.168.1.50"
if not is_active:
    result = "Доступ запрещен: аккаунт неактивен"
elif user_role == "admin":
    result = "Полный доступ"
elif user_role == "user" and ip_address.startswith("192.168"):
    result = "Доступ к локальной сети"
else:
    result = "Доступ запрещен"

print(f"Роль: {user_role}, Активен: {is_active}, IP: {ip_address}")
print(f"Результат: {result}")   
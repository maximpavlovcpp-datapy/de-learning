from functools import wraps

def require_role(required_role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Предполагаем, что первым аргументом (args[0]) всегда передаётся словарь user
            user = args[0]
            
            # Проверяем роль:
            if user.get("role") != required_role:
                raise PermissionError("Access denied")
            
            # Если проверка пройдена, вызываем функцию и возвращаем её результат:
            return func(*args, **kwargs)
            
        return wrapper
    return decorator

# Тестовая функция
@require_role("admin")
def delete_database(user):
    return "Database deleted successfully!"

# Проверка:
admin_user = {"name": "Alice", "role": "admin"}
guest_user = {"name": "Bob", "role": "guest"}

print(delete_database(admin_user))
# print(delete_database(guest_user)) # Должно выбросить PermissionError: Access denied
import psycopg2
import pandas as pd

# Параметры подключения к нашему Docker-контейнеру
conn_params = {
    "host": "localhost",
    "database": "learn",
    "user": "postgres",
    "password": "postgres",
    "port": "5432"
}

try:
    # 1. Подключаемся к базе
    conn = psycopg2.connect(**conn_params)
    print("Успешное подключение к PostgreSQL!")

    # 2. Выполняем SQL-запрос и сразу превращаем его в DataFrame
    query = "SELECT * FROM students;"
    df = pd.read_sql(query, conn)
    
    # 3. Выводим результат в консоль
    print("\nДанные из таблицы students:")
    print(df)

    # 4. Закрываем соединение
    conn.close()
    print("\nСоединение закрыто.")

except Exception as e:
    print(f"ОШИБКА: {e}")
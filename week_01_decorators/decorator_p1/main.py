from sqlalchemy import create_engine
import pandas as pd

# Формат строки подключения: диалект+драйвер://пользователь:пароль@хост:порт/база
DB_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/learn"

try:
    # Создаем движок (Engine). Он управляет пулом соединений.
    engine = create_engine(DB_URL)
    
    print("Движок SQLAlchemy создан. Выполняем запрос...")

    # Pandas теперь берет соединение из пула SQLAlchemy, а не создает сырое подключение
    query = "SELECT * FROM students;"
    df = pd.read_sql(query, engine)
    
    print("\nДанные из таблицы students:")
    print(df)

    # Движок не требует ручного закрытия, SQLAlchemy сама вернет соединение в пул
    print("\nЗапрос выполнен успешно.")

except Exception as e:
    print(f"ОШИБКА: {e}")
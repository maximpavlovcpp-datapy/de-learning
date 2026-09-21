from sqlalchemy import create_engine, text

DB_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/learn"
engine = create_engine(DB_URL)

def insert_students():
    # Открываем соединение
    with engine.connect() as conn:
        # Используем цикл for для добавления 5 студентов
        for i in range(1, 6):
            name = f"Student_{i}"
            age = 20 + i
            
            # Выполняем SQL-запрос на вставку
            # text() нужен для безопасной передачи параметров (защита от SQL-инъекций)
            conn.execute(
                text("INSERT INTO students (name, age) VALUES (:name, :age)"),
                {"name": name, "age": age}
            )
        
        # ВАЖНО: SQLAlchemy не сохраняет изменения автоматически. Нужен commit.
        conn.commit()
        print("Успешно добавлено 5 новых студентов в базу данных!")

if __name__ == "__main__":
    insert_students()
import sqlite3
from sqlite3 import Connection
from pathlib import Path

DB_FILENAME = "business_trip.db"

def init_db(conn: Connection):
    """Создаёт таблицу, если она ещё не существует."""
    conn.execute("""
        CREATE TABLE IF NOT EXISTS expense_articles (
            order_number   INTEGER PRIMARY KEY,    -- № приказа
            last_name      TEXT    NOT NULL,      -- Фамилия
            destination    TEXT    NOT NULL,      -- Место командировки
            payment        REAL    NOT NULL,      -- Оплата
            advance        REAL    NOT NULL,      -- Аванс
            expense_type   TEXT    NOT NULL,      -- Вид расходов
            total_amount   REAL    NOT NULL       -- Сумма расходов
        );
    """)
    conn.commit()

def add_record(conn: Connection):
    """Запрашивает данные у пользователя и добавляет новую запись."""
    print("\nДобавление новой статьи расхода:")
    order = int(input("  № приказа: "))
    last_name = input("  Фамилия: ").strip()
    dest = input("  Место командировки: ").strip()
    payment = float(input("  Оплата: "))
    advance = float(input("  Аванс: "))
    exp_type = input("  Вид расходов: ").strip()
    total = float(input("  Сумма расходов: "))

    conn.execute("""
        INSERT INTO expense_articles
        (order_number, last_name, destination, payment, advance, expense_type, total_amount)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (order, last_name, dest, payment, advance, exp_type, total))
    conn.commit()
    print("✅ Запись успешно добавлена.")

def view_all(conn: Connection):
    """Выводит все записи из таблицы."""
    print("\nВсе статьи расходов:")
    cursor = conn.execute("SELECT * FROM expense_articles ORDER BY order_number")
    rows = cursor.fetchall()
    if not rows:
        print("  (записей нет)")
        return
    for r in rows:
        print(f"  Приказ #{r[0]}: {r[1]}, {r[2]}, Оплата={r[3]}, Аванс={r[4]}, "
              f"{r[5]}, Сумма={r[6]}")

def find_by_last_name(conn: Connection):
    """Ищет записи по фамилии."""
    name = input("\nВведите фамилию для поиска: ").strip()
    cursor = conn.execute("""
        SELECT * FROM expense_articles
        WHERE last_name LIKE ?
        ORDER BY order_number
    """, (f"%{name}%",))
    rows = cursor.fetchall()
    if not rows:
        print("  По запросу ничего не найдено.")
        return
    print(f"Результаты поиска по «{name}»:")
    for r in rows:
        print(f"  #{r[0]}: {r[1]}, {r[2]}, Сумма расходов={r[6]}")

def main():
    db_path = Path(__file__).parent / DB_FILENAME
    conn = sqlite3.connect(str(db_path))
    init_db(conn)

    menu = {
        "1": ("Добавить запись", add_record),
        "2": ("Показать все записи", view_all),
        "3": ("Найти по фамилии", find_by_last_name),
        "0": ("Выход", None)
    }

    while True:
        print("\n=== Меню ===")
        for key, (text, _) in menu.items():
            print(f"  {key}. {text}")
        choice = input("Выберите пункт: ").strip()
        if choice == "0":
            print("До встречи!")
            break
        action = menu.get(choice)
        if not action:
            print("❗ Неверный пункт, попробуйте ещё.")
            continue
        action[1](conn)

    conn.close()

if __name__ == "__main__":
    main()

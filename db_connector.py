import sqlite3

try:
    db = sqlite3.connect("tg_bot_db.db", check_same_thread=False)
    cursor = db.cursor()
except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)


def add_chat_id(chat_id: str):
    cursor.execute(
        """INSERT INTO bot_users(chat_id, subscribed) VALUES(?, ?)""",
        (chat_id, 0)
    )
    db.commit()


def remove_chat_id(chat_id: str):
    cursor.execute(
        """DELETE FROM bot_users WHERE chat_id = ?""", (chat_id,)
    )
    db.commit()


def add_sub(chat_id: str):
    cursor.execute(
        """UPDATE bot_users SET subscribed = 1 WHERE chat_id = ?""", (chat_id, )
    )
    db.commit()


def remove_sub(chat_id: str):
    cursor.execute(
        """UPDATE bot_users SET subscribed = 0 WHERE chat_id = ?""", (chat_id, )
    )
    db.commit()


def get_subs():
    cursor.execute(
        """SELECT chat_id FROM bot_users WHERE subscribed = 1"""
    )
    subs = [value[0] for value in cursor.fetchall()]
    return subs

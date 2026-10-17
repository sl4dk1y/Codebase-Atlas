"""SQLite persistence function for the fictional registration sample."""


def insert_user(connection, name: str, email: str) -> int:
    """Insert a user using the caller's SQLite connection.

    The caller is responsible for providing a connection whose database has a
    users table with an integer primary key and name/email columns.
    """
    cursor = connection.execute(
        "INSERT INTO users (name, email) VALUES (?, ?)",
        (name, email),
    )
    connection.commit()
    return int(cursor.lastrowid)

"""Registration business logic for the fictional sample."""

import database


def register_user(connection, name: str, email: str) -> int:
    """Normalize registration values and persist one user."""
    return database.insert_user(connection, name.strip(), email.strip().lower())

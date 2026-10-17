"""Entry point for the fictional registration sample; not run by the skill."""

from sqlite3 import Connection

import handlers


def register_user_request(request: dict[str, str], connection: Connection) -> dict[str, int]:
    """Pass a registration request to its handler and return the response."""
    return handlers.handle_registration(request, connection)

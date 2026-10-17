"""Request handling for the fictional registration sample."""

import services


def handle_registration(request: dict[str, str], connection) -> dict[str, int]:
    """Create a user from request fields and return a simple response."""
    user_id = services.register_user(
        connection,
        name=request["name"],
        email=request["email"],
    )
    return {"status": 201, "user_id": user_id}

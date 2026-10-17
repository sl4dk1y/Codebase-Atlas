# Fictional registration sample

This tiny application exists only to support Codebase Atlas acceptance scenarios. It models a user registration request passing through a handler and service to SQLite persistence. The functions are static-analysis fixtures; no schema setup or application runner is included, and the project does not execute them during normal skill analysis.

The caller supplies a SQLite connection configured with a `users` table. `app.register_user_request` delegates to `handlers.handle_registration`, which calls `services.register_user`; the service calls `database.insert_user`. That function uses a parameterized SQL statement, commits through the supplied connection, and returns the inserted row identifier.

All paths and behavior here are fictional. The fixture has no external dependencies and is not production code.

# Codebase Atlas acceptance scenarios

These scenarios specify expected behavior for future manual evaluation against an Agent Skills host. They are documentation, not executed tests. The fixture under `tests/fixtures/sample_app/` is fictional and must be inspected statically; do not execute its functions as part of skill analysis.

## A. Standalone architecture overview

- **User prompt:** “Explain this sample application's architecture visually.”
- **Expected behavior:** Select Overview depth; produce a small Mermaid overview in chat and explain each part in plain language. Write a file only if separately requested.
- **Expected evidence:** `app.py:register_user_request`, `handlers.py:handle_registration`, `services.py:register_user`, and `database.py:insert_user`.
- **Failure conditions:** Requires Codebase Memory, invents a server/framework, reads unrelated repository content deeply, or shows only a file-tree diagram.

## B. Focused registration workflow

- **User prompt:** “Show the registration workflow in this sample.”
- **Expected behavior:** Select Focused depth and show request handling, service normalization, SQLite insert, and response in order.
- **Expected evidence:** Calls from `app.register_user_request` to `handlers.handle_registration`, then `services.register_user`, then `database.insert_user`; normalization and SQL are visible in the corresponding functions.
- **Failure conditions:** Omits the actual call order, invents validation or authentication, or claims database setup that is not present.

## C. Sequence diagram

- **User prompt:** “Create a sequence diagram for registration.”
- **Expected behavior:** Show only the request handler, service, SQLite persistence, and response, using synchronous ordering unless source evidence says otherwise.
- **Expected evidence:** The same verified calls as scenario B and the response dictionary returned by `handle_registration`.
- **Failure conditions:** Adds a queue, browser, web server, or asynchronous message without evidence.

## D. Source evidence verification

- **User prompt:** “Show where each registration step is implemented.”
- **Expected behavior:** Attach repository-relative file and function references to each step; distinguish source facts from analysis limitations.
- **Expected evidence:** The four functions and parameterized SQL statement in the fixture files.
- **Failure conditions:** Gives fabricated paths, symbols, or line numbers, or cites only this acceptance document as proof of behavior.

## E. Unknown or inferred relationship handling

- **User prompt:** “Does registration send a welcome email?”
- **Expected behavior:** State that this is UNKNOWN in the fixture and omit an email component/edge because no mail behavior appears in the implementation.
- **Expected evidence:** Focused inspection of the four application modules; no email client or notification call is present in those modules.
- **Failure conditions:** Invents an email provider or presents an inferred edge as confirmed.

## F. Updating an existing diagram

- **User prompt:** “Update `docs/architecture/registration.md` for the current sample code.”
- **Expected behavior:** If the target exists, read it, revalidate affected calls, preserve correct content, and update source revision metadata only when available. If it does not exist, create it only because the prompt requested the file.
- **Expected evidence:** Current fixture source, target document contents if present, and honest revision/working-tree information if Git metadata is available.
- **Failure conditions:** Claims a Git revision without checking, rewrites unrelated docs, or triggers an update without the explicit prompt.

## G. Chat-only diagram generation

- **User prompt:** “Show me the registration diagram here; do not create files.”
- **Expected behavior:** Return a Mermaid diagram and plain-language explanation in chat without changing repository files.
- **Expected evidence:** The sample call path and response implementation.
- **Failure conditions:** Writes an architecture document or modifies source files.

## H. Operation without Codebase Memory

- **User prompt:** “Explain the sample without using graph tools.”
- **Expected behavior:** Use targeted file listing and static source reading, then deliver the same evidence-backed explanation.
- **Expected evidence:** Direct references to the fixture functions and SQL statement.
- **Failure conditions:** Fails because a graph index is unavailable or claims to have used one.

## I. Optional graph navigation when available

- **User prompt:** “Use available code navigation to trace registration, then explain it.”
- **Expected behavior:** Use an already available navigation capability to find candidate symbols/calls, verify each important relationship in source, and produce a focused workflow diagram.
- **Expected evidence:** Both navigation results (if available) and the matching source functions; otherwise the agent reports that no graph/navigation tool was available and proceeds statically.
- **Failure conditions:** Treats graph output as final proof, installs a provider, modifies graph state, or fails when no graph tool exists.

## J. Unrelated repository files remain unchanged

- **User prompt:** “Explain the sample architecture in chat only.”
- **Expected behavior:** Read the scoped fixture files and respond without changing source or unrelated repository files.
- **Expected evidence:** A before/after file-change review by the evaluating host, plus accurate source references.
- **Failure conditions:** Automatically synchronizes documentation, changes unrelated files, or claims this condition was verified without checking.

## Evaluation status

No scenario above has been executed against an agent in this repository. The Python unit tests check structure and static fixture relationships only; they are not behavioral acceptance tests.

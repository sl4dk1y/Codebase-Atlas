# Mermaid conventions

Mermaid in fenced Markdown is the canonical format. Use conservative syntax supported by GitHub's Mermaid integration. The skill does not include a custom renderer; rendering in other hosts depends on their support.

## Rules

- Use a fenced block such as ` ```mermaid ` followed by `flowchart TD`, `sequenceDiagram`, or `erDiagram`.
- Use simple identifiers (`WebApp`, `Database`) and quote display labels when they contain spaces: `API["Public API"]`.
- Keep direction and arrow meaning consistent. Label arrows when the interaction or data matters.
- Use solid arrows for confirmed relationships. A dashed edge may represent an inferred relationship only when visibly labeled and explained in text.
- Keep a node's conceptual meaning stable. Avoid duplicate nodes for one component unless boundaries are explicitly distinct.
- Use a database-shaped node such as `DB[("Application database")]` in a flowchart when an ER diagram is not needed.
- Use `erDiagram` for schema relationships and common cardinality syntax such as `||--o{` only when cardinality is supported.
- In sequence diagrams, write explicit messages. Use `->>` for a message only when its notation does not falsely imply unverified async behavior; describe async semantics separately only when confirmed.
- Avoid HTML, custom theme directives, icons, external includes, click actions, and renderer-specific extensions.
- Escape or rephrase labels containing syntax-sensitive punctuation.

## Validation

Before delivery, check that:

1. The fenced Mermaid block opens and closes.
2. Every arrow endpoint is a declared node (ER diagrams use declared entities).
3. The diagram type matches the request.
4. Labels are clear and edges correspond to evidence.
5. The diagram fits the chosen scope and remains readable in plain text.

If a Mermaid CLI or host renderer is already available and using it is safe, it may be used as an optional check. Never install one automatically. If not used, report that only structural review was performed; do not claim rendered validation.

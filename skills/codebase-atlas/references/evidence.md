# Evidence, uncertainty, and document shape

## Evidence states

- **CONFIRMED** — directly supported by current source code, configuration, schema, or tests. Use normal edges and state the source.
- **INFERRED** — a plausible reading of partial evidence. Label the relevant node/edge or list it under assumptions; use a dashed edge when useful. Explain what evidence is missing.
- **UNKNOWN** — insufficient evidence. Omit from the main diagram in most cases. If the gap matters, say it remains unknown.

Prior docs, memory notes, and graph/index results can guide navigation but are not current implementation evidence by themselves. Verify important claims against source. Do not promote an inferred relationship to confirmed just to make a diagram complete.

## Source references

Prefer repository-relative paths and useful symbol names, for example:

```text
Implementation: src/alerts/dispatcher.py
Symbols: AlertDispatcher.send_alert, format_message
```

Add line numbers only when verified. Do not include machine-specific absolute paths, credentials, tokens, or private configuration values. A source reference should let a maintainer locate the evidence without reading an entire repository.

## Recommended document structure

````markdown
# [Architecture or workflow name]

## What this diagram explains
[Short plain-language purpose]

## Architecture diagram
```mermaid
flowchart TD
    ...
````

## How it works
1. [Verified step]

## Main components
- **[Component]** — [responsibility]. Source: `relative/path` (`Symbol`).

## Assumptions and uncertainties
- [Only material inferred/unknown facts]

## Verification and limitations
- [What was checked and what was not]

## Source revision
- Commit: [SHA or unavailable]
- Branch: [branch or unavailable]
- Generated: [date]
- Working-tree changes included: [yes/no/unknown]
```

For a small chat response, use a shorter form but retain a purpose, diagram, explanation, real source references, and material uncertainty. Do not invent revision metadata.

## Plain-language explanation

Explain what each major component does and why data moves along each edge. Define necessary technical terms in place. Distinguish implementation facts from analysis limitations. Be concise, but make the model understandable without requiring the reader to decode the source first.

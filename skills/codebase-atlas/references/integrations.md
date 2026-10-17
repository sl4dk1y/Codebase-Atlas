# Optional integrations

Codebase Atlas is standalone-first. Optional navigation or project context may reduce search effort, but never becomes a prerequisite or a substitute for current source evidence.

## Code navigation and graph tools

At the start of a relevant task, determine whether the existing host already exposes code search, symbol lookup, call graphs, dependency graphs, AST navigation, or a language server. Use available capabilities to locate likely entry points, symbols, relationships, dependencies, and data flows. Verify important relationships in the current source before presenting them as confirmed. Graph coverage may be incomplete or stale.

Do not assume a provider's command, schema, installation method, or persistence model. Do not require a persistent graph database, build a duplicate graph engine, modify graph state, or install a provider. When no tool is available, use targeted repository listing, text search, configuration/manifests, tests, schema files, and direct source reading.

### Codebase Memory

Codebase Memory may accelerate symbol and call-path discovery when already available. It is optional. Do not assume specific commands or APIs, require installation, copy its internal graph, change its persistent state, or treat graph output as verified architecture. Check its discoveries against current source.

## Agent Safe Flow

An orchestrator such as Agent Safe Flow may route explicit user requests such as “generate an architecture diagram,” “explain this subsystem visually,” or “update the existing workflow diagram” to Codebase Atlas. Atlas performs the requested visualization only. This integration does not authorize documentation synchronization outside the requested scope, Context Waypoint or graph updates, Git operations, deployment, or publication.

Reusable routing snippet for a host's `AGENTS.md` (adapt to that host; it is not an executable API):

```markdown
When explicitly requested to create, explain, or update human-readable architecture diagrams, use the installed `codebase-atlas` skill if available.

Follow its `SKILL.md` instructions. Do not assume a fixed installation directory. Do not automatically generate or update diagrams during unrelated development tasks. If the skill is unavailable, report that limitation without claiming it was executed.
```

### Source, installation, and discovery paths

The routing snippet is intentionally host-neutral for Codex, Claude Code, and compatible Agent Skills hosts: it invokes the skill by name, then lets the host's supported discovery mechanism find it.

- **Source repository path** — in this repository, the skill source is `skills/codebase-atlas/SKILL.md`. This path helps maintainers edit this project; it is not a universal path in consumer repositories.
- **Installed skill path** — a copy of the skill has `SKILL.md` at the root of its own skill directory. The parent directory is chosen by the installer or user and can vary by host and setup.
- **Host-specific discovery** — agents may discover skills through host conventions, configured directories, or explicit skill selection. Ask the host to locate `codebase-atlas` by name or consult that host's current skill documentation. Do not assume a particular directory such as `~/.agents/skills`.

This project does not automatically edit external repositories or orchestrator configuration.

## Context Waypoint

Context Waypoint may provide recent project state, decisions, or known architecture changes. Treat that material as search context, not authoritative evidence of current runtime behavior. Verify important claims against source. Do not require Context Waypoint, alter its data, or assume a specific host integration.

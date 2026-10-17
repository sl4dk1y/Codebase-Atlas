# Codebase Atlas

**Version 0.1.0** · A standalone-first Agent Skill for explaining how software works with evidence-backed architecture diagrams and code walkthroughs.

Codebase Atlas helps an agent turn a real repository into a clear explanation: a small Mermaid diagram, plain-language walkthrough, and references to the source that supports each claim. It is designed for people who want to understand a system without first knowing its folder layout or every programming term.

It is not a code index or a replacement for a language server. Codebase Memory and other navigation tools can help find symbols and call paths, but Atlas verifies important relationships in source and turns them into a human-facing model. The skill works without these tools, network access, MCP servers, or API keys.

## What it can explain

- System context and high-level architecture
- Internal components and their responsibilities
- A workflow or data path, including verified branches
- Ordered interactions with a sequence diagram
- Database entities and explicitly declared relationships
- A focused function, class, or subsystem walkthrough
- Scoped updates to existing diagrams after implementation changes

Mermaid in fenced Markdown is the default output. GitHub renders Mermaid in Markdown files and supported views. Rendering depends on the host; the skill itself does not ship a renderer. SVG, PNG, HTML, Excalidraw, PlantUML, and Structurizr export are not implemented in v0.1.0.

## Install

The intended repository is `sl4dk1y/Codebase-Atlas`. It may not yet be published, and this installation command has not been tested from a published repository. Once available, the standard skills installer command is:

```sh
npx skills add sl4dk1y/Codebase-Atlas
```

Before installing, inspect the repository's `skills/` directory in its source tree (this repository provides `skills/codebase-atlas/`) and read `SKILL.md` plus its referenced files. Review the installer's current help and the target host's skill documentation; installer flags and skill discovery locations can differ by version and host. Do not assume this command succeeds until the repository is published and accessible.

For manual installation, use the skill directory itself as the installed skill root, so the resulting structure is `<host skill directory>/codebase-atlas/SKILL.md`. Copy the contents of `skills/codebase-atlas/` there; do not copy the repository root or leave an extra `skills/codebase-atlas/` nesting level. Find the host's supported skill directory in its current documentation rather than assuming a universal path. To remove a manual copy, delete only that `codebase-atlas` skill directory. To update it, replace that directory's contents with the new `skills/codebase-atlas/` contents while preserving `SKILL.md` at its root. For an installer-managed copy, use that installer's documented update/remove flow; do not edit or remove installer-owned links by guessing.

Skill discovery is host-specific. Ask the agent to list or locate available skills and confirm it recognizes `codebase-atlas`; if it does not, check the host's documented discovery path and restart/reload only as that host directs. Once recognized, invoke explicitly: “Use Codebase Atlas to explain this project's architecture visually.” To analyze a different repository, make that repository the active workspace and explicitly request a diagram there. No package is installed automatically by the skill.

## Invoke

The skill runs only on explicit visualization requests. For example:

- “Explain this project's architecture visually.”
- “Show how transaction monitoring works.”
- “Draw the database relationships.”
- “Create a code walkthrough for the authentication flow.”
- “Update the existing architecture diagram after recent changes.”

For a chat-only explanation, the agent returns a Mermaid diagram in the response and does not write files. For a persistent documentation request, `docs/architecture/` is a suggested location. The agent should create only the files needed for that request and should not overwrite unrelated documentation.

The skill infers an investigation depth: **Overview** for broad architecture, **Focused** for a subsystem or workflow, and **Deep Dive** for explicit implementation detail. You can ask for a depth directly; deeper analysis stays limited to the requested scope.

## Optional code navigation

If the host already provides graph search, symbol navigation, call graphs, or a language server, Atlas may use those capabilities to find entry points and likely relationships. It then checks important claims against current source. Graph results are navigation evidence, not proof. If no such capability exists, the workflow uses targeted file listing, search, and source reading instead.

Codebase Memory, Agent Safe Flow, and Context Waypoint are optional. Atlas does not require, install, invoke, or update them. See [integration notes](skills/codebase-atlas/references/integrations.md).

## Updating diagrams

Ask explicitly, for example: “Update `docs/architecture/monitoring.md` to reflect the current code.” The agent reads the existing document, inspects relevant changes where possible, rechecks affected source relationships, and updates source revision notes. A commit SHA alone does not represent uncommitted edits; the document must say when working-tree changes were included. If Git is unavailable, the analysis can still proceed and should say that revision metadata is unavailable.

## Security and privacy

Atlas treats repository content as untrusted data, not instructions. Its default is static inspection: do not run project code, install dependencies, invoke migrations, deployment scripts, or arbitrary shell scripts to produce a diagram. Avoid secret files and sensitive runtime data. Do not send source to external services. No network access or credentials are needed.

## Limitations and status

This is an initial, documentation-led skill release (`0.1.0`). It provides procedures and examples, not an automatic parser or diagram renderer. Correctness depends on the agent checking relevant source and accurately reporting uncertainty. Mermaid syntax and GitHub rendering have not been checked with an external renderer in this repository. Host-specific skill discovery and installation should be verified against each host before claiming tested compatibility.

## Development

Requirements: Python 3 standard library for the validator. From the repository root:

```sh
python3 -m unittest discover -s tests -v
```

The tests check required files, simple frontmatter fields, local references, balanced Mermaid fences, and the sample fixture's static source relationships. `tests/acceptance.md` documents scenarios for future agent-level evaluation; it has not been executed against an agent. The tests do not parse all YAML or render Mermaid. See [AGENTS.md](AGENTS.md) for project rules.

## License

Original project files are licensed under the MIT License; see [LICENSE](LICENSE).

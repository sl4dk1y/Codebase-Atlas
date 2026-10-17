# Choosing a diagram

Select a diagram based on what the reader needs to understand, not on terminology the user may not know. Mermaid flowcharts can represent C4-inspired levels when boundaries are clear.

| User's question | View | Show |
| --- | --- | --- |
| “How does this app work?” | System overview / System Context | Users, system boundary, major subsystems, external systems, stores; usually 5–12 nodes |
| “What are its main parts?” | Component architecture / Container | Meaningful internal components, responsibilities, verified dependencies and boundaries |
| “What happens when I do X?” | Workflow / data flow | Actual processing order, meaningful verified decisions, data movement, outputs |
| “Who talks to whom and when?” | Sequence | Only verified participants and ordered messages; distinguish async only when proven |
| “How are records related?” | Database ER | Entities and declared relationship cardinality from schema/models/migrations |
| “How does this function/subsystem work?” | Code-level walkthrough | Relevant files/symbols, inputs, outputs, calls, side effects, errors |

## System overview (C4-inspired System Context)

Use a single boundary around the system in scope. Place human or external actors outside it. Group internal detail rather than exposing every module. Name external systems only when actual code/configuration establishes their presence. A store may appear if it matters to the system-level explanation.

## Component architecture (C4-inspired Container or Component)

Choose the level requested. In C4, “container” means an independently executable/deployable application or data store, not a Docker container. A component is a coherent responsibility inside an application boundary. Do not mix levels without labeling the diagram. For a small service, show components; for a multi-process system, show applications/processes and stores.

## Workflow and sequence

Use a flowchart for decisions, transformations, and data movement. Use a sequence diagram when participant order over time is the main point. Neither should imply a runtime trace unless evidence comes from one; static source supports implemented paths, not proof that a path occurred in production.

## Database relationships

Use Mermaid `erDiagram` where appropriate. Include columns only when they help explain the model. Draw relationships only when a foreign key, ORM relationship declaration, or equivalent explicit schema evidence exists. Similar field names alone do not establish a relationship.

## Code walkthrough

A walkthrough may pair a small diagram with numbered prose. Cite relevant symbols and files; explain inputs, outputs, side effects, and error handling only when inspected. Do not paste whole files or imply one call path is exhaustive unless it was checked.

## Complexity

Aim for 5–12 nodes for overviews and 5–15 for subsystem diagrams; 20 nodes is a soft ceiling. If more detail is necessary, split by subsystem or workflow. Correctness takes priority over node count. Use readable labels instead of unexplained abbreviations.

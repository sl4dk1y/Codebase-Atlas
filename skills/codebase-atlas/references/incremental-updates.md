# Updating existing diagrams

Run this workflow only after an explicit update request. A code change by itself does not authorize an architecture documentation update.

1. Read the target document and its source revision notes.
2. Determine available revision metadata with read-only Git inspection, if Git exists. Do not assume a clean tree or that a SHA covers uncommitted edits.
3. Inspect changes relevant to the diagram when a reliable diff is available. Use a scoped reanalysis if not.
4. Identify affected components, edges, workflow steps, and source references.
5. Recheck each affected relationship against current source. Preserve content that remains correct.
6. Edit only the requested documentation. Keep unrelated material intact.
7. Update revision metadata: commit SHA, branch when relevant, generation date, and whether working-tree modifications were included. If unavailable, state that rather than fabricating it.
8. Report what changed and what could not be verified.

If Git is absent, analyze current source normally and note that revision tracking is unavailable. If uncommitted changes are included, do not describe the output as representing only the recorded commit. Never run Git write operations or fabricate revision history.

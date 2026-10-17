"""Lightweight structural checks for the Codebase Atlas skill."""

import ast
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "codebase-atlas"
SKILL_FILE = SKILL_DIR / "SKILL.md"
REFERENCE_FILES = (
    "investigation.md",
    "diagram-types.md",
    "mermaid.md",
    "evidence.md",
    "incremental-updates.md",
    "integrations.md",
)
EXAMPLE_FILES = (
    "system-overview.md",
    "component-architecture.md",
    "workflow.md",
    "sequence.md",
    "database.md",
)
REQUIRED_ROOT_FILES = (
    "README.md",
    "README.ru.md",
    "LICENSE",
    "AGENTS.md",
    ".gitignore",
)


def markdown_files():
    return sorted(ROOT.rglob("*.md"))


def extract_frontmatter(text):
    """Read only the simple scalar fields required by this project."""
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end < 0:
        return None
    fields = {}
    for line in text[4:end].splitlines():
        match = re.fullmatch(r"([A-Za-z][A-Za-z0-9_-]*):\s*(.*?)\s*", line)
        if match:
            fields[match.group(1)] = match.group(2)
    return fields


def called_names(source, function_name):
    """Return call targets in one function without importing or executing it."""
    tree = ast.parse(source)
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == function_name:
            names = set()
            for child in ast.walk(node):
                if isinstance(child, ast.Call):
                    if isinstance(child.func, ast.Name):
                        names.add(child.func.id)
                    elif isinstance(child.func, ast.Attribute):
                        names.add(child.func.attr)
            return names
    raise AssertionError(f"function {function_name!r} was not found")


class SkillStructureTests(unittest.TestCase):
    def test_required_repository_files_exist(self):
        for relative in REQUIRED_ROOT_FILES:
            with self.subTest(path=relative):
                self.assertTrue((ROOT / relative).is_file())
        self.assertTrue(SKILL_FILE.is_file())

    def test_frontmatter_name_and_description(self):
        fields = extract_frontmatter(SKILL_FILE.read_text(encoding="utf-8"))
        self.assertIsNotNone(fields, "SKILL.md must start with YAML frontmatter")
        self.assertEqual(fields.get("name"), "codebase-atlas")
        description = fields.get("description", "")
        self.assertTrue(description.strip())
        self.assertLessEqual(len(description), 1024)

    def test_referenced_documents_exist(self):
        skill_text = SKILL_FILE.read_text(encoding="utf-8")
        referenced = re.findall(r"`((?:references|examples)/[^`]+\.md)`", skill_text)
        self.assertTrue(referenced, "SKILL.md should link its detailed documents")
        for relative in referenced:
            with self.subTest(path=relative):
                self.assertTrue((SKILL_DIR / relative).is_file())
        for name in REFERENCE_FILES:
            with self.subTest(path=name):
                self.assertTrue((SKILL_DIR / "references" / name).is_file())
        for name in EXAMPLE_FILES:
            with self.subTest(path=name):
                self.assertTrue((SKILL_DIR / "examples" / name).is_file())

    def test_markdown_fences_are_balanced(self):
        for path in markdown_files():
            lines = path.read_text(encoding="utf-8").splitlines()
            fence = None
            for line_number, line in enumerate(lines, start=1):
                match = re.match(r"^\s*(`{3,}|~{3,})(.*)$", line)
                if not match:
                    continue
                marker = match.group(1)[0]
                if fence is None:
                    fence = marker
                elif marker == fence:
                    fence = None
            with self.subTest(path=path.relative_to(ROOT)):
                self.assertIsNone(fence, "unclosed fenced code block")

    def test_no_mandatory_vendor_dependency_is_declared(self):
        # The project has no package manifests; this guards against introducing
        # an explicit mandatory provider requirement in the skill itself.
        skill_text = SKILL_FILE.read_text(encoding="utf-8").lower()
        for phrase in ("requires codebase memory", "requires agent safe flow",
                       "requires context waypoint", "requires mcp server"):
            with self.subTest(phrase=phrase):
                self.assertNotIn(phrase, skill_text)
        self.assertFalse((ROOT / "package.json").exists())
        self.assertFalse((ROOT / "pyproject.toml").exists())
        self.assertFalse((ROOT / "requirements.txt").exists())

    def test_skill_file_links_are_relative(self):
        text = SKILL_FILE.read_text(encoding="utf-8")
        references = re.findall(r"`((?:references|examples)/[^`]+\.md)`", text)
        for reference in references:
            with self.subTest(reference=reference):
                path = Path(reference)
                self.assertFalse(path.is_absolute())
                self.assertNotIn("..", path.parts)

    def test_readme_install_commands_match(self):
        commands = []
        for name in ("README.md", "README.ru.md"):
            text = (ROOT / name).read_text(encoding="utf-8")
            matches = re.findall(r"npx skills add [^\s`]+", text)
            self.assertEqual(matches, ["npx skills add sl4dk1y/Codebase-Atlas"])
            commands.append(matches[0])
        self.assertEqual(commands[0], commands[1])

    def test_local_markdown_links_resolve(self):
        for document in markdown_files():
            text = document.read_text(encoding="utf-8")
            links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", text)
            for target in links:
                if target.startswith(("http://", "https://", "#")):
                    continue
                local_target = target.split("#", 1)[0]
                with self.subTest(document=document.relative_to(ROOT), target=target):
                    self.assertTrue((document.parent / local_target).exists())

    def test_acceptance_scenarios_and_static_fixture_relationships(self):
        acceptance = ROOT / "tests" / "acceptance.md"
        self.assertTrue(acceptance.is_file())
        acceptance_text = acceptance.read_text(encoding="utf-8")
        for label in "ABCDEFGHIJ":
            with self.subTest(scenario=label):
                self.assertIn(f"## {label}.", acceptance_text)
        self.assertIn("executed against an agent", acceptance_text)

        fixture = ROOT / "tests" / "fixtures" / "sample_app"
        expected_files = ("app.py", "handlers.py", "services.py", "database.py", "README.md")
        for name in expected_files:
            with self.subTest(fixture_file=name):
                self.assertTrue((fixture / name).is_file())

        source = {
            name: (fixture / name).read_text(encoding="utf-8")
            for name in expected_files if name.endswith(".py")
        }
        for text in source.values():
            ast.parse(text)
        self.assertIn("handle_registration", called_names(source["app.py"], "register_user_request"))
        self.assertIn("register_user", called_names(source["handlers.py"], "handle_registration"))
        service_calls = called_names(source["services.py"], "register_user")
        self.assertIn("insert_user", service_calls)
        database_calls = called_names(source["database.py"], "insert_user")
        self.assertIn("execute", database_calls)
        self.assertIn("commit", database_calls)
        self.assertIn("?", source["database.py"])


if __name__ == "__main__":
    unittest.main()

"""Small AST security check for this standard-library-only lab application."""
import ast
from pathlib import Path
import sys


def scan():
    violations = []
    for path in Path("src").rglob("*.py"):
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                if node.func.id in {"eval", "exec"}:
                    violations.append(f"{path}:{node.lineno}: forbidden {node.func.id}")
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                if isinstance(node.func.value, ast.Name):
                    owner = node.func.value.id
                    if (owner == "pickle" and node.func.attr in {"load", "loads"}) or (owner == "os" and node.func.attr == "system"):
                        violations.append(f"{path}:{node.lineno}: unsafe call")
            if isinstance(node, ast.Call):
                if any(k.arg == "shell" and isinstance(k.value, ast.Constant) and k.value.value is True for k in node.keywords):
                    violations.append(f"{path}:{node.lineno}: shell=True")
    return violations


if __name__ == "__main__":
    findings = scan()
    print("\n".join(findings) if findings else "PASS: no prohibited constructs in src")
    sys.exit(bool(findings))

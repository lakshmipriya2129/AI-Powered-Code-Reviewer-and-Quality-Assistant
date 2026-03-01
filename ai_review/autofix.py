import re


class AutoFixEngine:

    # -------------------------
    # Fix naming convention
    # -------------------------
    def fix_function_names(self, code):

        def snake_case(name):
            s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
            return re.sub('([a-z0-9])([A-Z])',
                          r'\1_\2', s1).lower()

        pattern = r"def ([A-Za-z0-9]+)\("

        def repl(match):
            return f"def {snake_case(match.group(1))}("

        return re.sub(pattern, repl, code)

    # -------------------------
    # Add Missing Docstrings
    # -------------------------
    def add_docstrings(self, code):

        lines = code.split("\n")
        updated = []

        for i, line in enumerate(lines):
            updated.append(line)

            if line.strip().startswith("def "):
                updated.append('    """Auto-generated docstring."""')

        return "\n".join(updated)

    # -------------------------
    # Fix spacing
    # -------------------------
    def fix_spacing(self, code):
        return re.sub(r"\n{3,}", "\n\n", code)


def apply_autofix(code):
    fixer = AutoFixEngine()

    code = fixer.fix_function_names(code)
    code = fixer.add_docstrings(code)
    code = fixer.fix_spacing(code)

    return code
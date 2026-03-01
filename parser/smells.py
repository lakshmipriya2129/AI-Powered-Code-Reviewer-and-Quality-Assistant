import ast


class SmellDetector(ast.NodeVisitor):

    def __init__(self):
        self.smells = {
            "long_functions": [],
            "deep_nesting": [],
            "missing_type_hints": []
        }

    # -----------------------
    # Long Function Detection
    # -----------------------
    def visit_FunctionDef(self, node):

        length = node.end_lineno - node.lineno \
            if node.end_lineno else 0

        if length > 50:
            self.smells["long_functions"].append(
                (node.name, length)
            )

        # Missing type hints
        if not node.returns:
            self.smells["missing_type_hints"].append(node.name)

        nesting = self.calculate_nesting(node)
        if nesting > 3:
            self.smells["deep_nesting"].append(
                (node.name, nesting)
            )

        self.generic_visit(node)

    def calculate_nesting(self, node):
        max_depth = 0

        def visit(n, depth=0):
            nonlocal max_depth
            if isinstance(n, (ast.If, ast.For, ast.While)):
                depth += 1
                max_depth = max(max_depth, depth)

            for child in ast.iter_child_nodes(n):
                visit(child, depth)

        visit(node)
        return max_depth


def detect_smells(tree):
    detector = SmellDetector()
    detector.visit(tree)
    return detector.smells
import ast


class CoverageEstimator(ast.NodeVisitor):

    def __init__(self):
        self.functions = 0
        self.branches = 0

    def visit_FunctionDef(self, node):
        self.functions += 1
        self.generic_visit(node)

    def visit_If(self, node):
        self.branches += 1
        self.generic_visit(node)

    def visit_For(self, node):
        self.branches += 1
        self.generic_visit(node)


def estimate_coverage(tree):

    est = CoverageEstimator()
    est.visit(tree)

    if est.functions == 0:
        return 0

    coverage_hint = (
        est.functions * 10 +
        est.branches * 2
    )

    return min(100, coverage_hint)
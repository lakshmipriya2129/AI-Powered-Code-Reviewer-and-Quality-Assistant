import ast


class DependencyVisitor(ast.NodeVisitor):

    def __init__(self):
        self.imports = []

    def visit_Import(self, node):
        for alias in node.names:
            self.imports.append(alias.name)

    def visit_ImportFrom(self, node):
        module = node.module or ""
        self.imports.append(module)


def extract_dependencies(tree):
    visitor = DependencyVisitor()
    visitor.visit(tree)
    return list(set(visitor.imports))
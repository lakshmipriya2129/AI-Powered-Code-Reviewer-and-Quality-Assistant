import ast
from parser.models import (
    FunctionInfo,
    ClassInfo,
    FileAnalysis
)
from parser.complexity import calculate_complexity
from parser.dependency import extract_dependencies
from parser.smells import detect_smells


class CodeAnalyzer(ast.NodeVisitor):

    def __init__(self):
        self.functions = []
        self.classes = []

    # ----------------------
    # Function Extraction
    # ----------------------
    def visit_FunctionDef(self, node):

        args = [arg.arg for arg in node.args.args]

        complexity = calculate_complexity(node)

        has_types = any(
            arg.annotation for arg in node.args.args
        )

        func = FunctionInfo(
            name=node.name,
            lineno=node.lineno,
            args=args,
            complexity=complexity,
            has_type_hints=has_types
        )

        self.functions.append(func)
        self.generic_visit(node)

    # ----------------------
    # Class Extraction
    # ----------------------
    def visit_ClassDef(self, node):

        class_info = ClassInfo(
            name=node.name,
            lineno=node.lineno
        )

        for item in node.body:
            if isinstance(item, ast.FunctionDef):

                args = [a.arg for a in item.args.args]

                method = FunctionInfo(
                    name=item.name,
                    lineno=item.lineno,
                    args=args,
                    complexity=calculate_complexity(item),
                    has_type_hints=any(
                        a.annotation
                        for a in item.args.args
                    )
                )

                class_info.methods.append(method)

        self.classes.append(class_info)
        self.generic_visit(node)


# ===================================
# PUBLIC API
# ===================================

def analyze_file(filepath: str):

    with open(filepath, "r", encoding="utf-8") as f:
        source = f.read()

    tree = ast.parse(source)

    analyzer = CodeAnalyzer()
    analyzer.visit(tree)

    dependencies = extract_dependencies(tree)
    smells = detect_smells(tree)

    return FileAnalysis(
        filename=filepath,
        imports=dependencies,
        classes=analyzer.classes,
        functions=analyzer.functions,
        dependencies=dependencies,
        smells=smells
    )
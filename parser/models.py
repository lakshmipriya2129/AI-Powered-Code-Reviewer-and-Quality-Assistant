from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class FunctionInfo:
    name: str
    lineno: int
    args: List[str]
    complexity: int
    has_type_hints: bool


@dataclass
class ClassInfo:
    name: str
    lineno: int
    methods: List[FunctionInfo] = field(default_factory=list)


@dataclass
class FileAnalysis:
    filename: str
    imports: List[str]
    classes: List[ClassInfo]
    functions: List[FunctionInfo]
    dependencies: List[str]
    smells: Dict
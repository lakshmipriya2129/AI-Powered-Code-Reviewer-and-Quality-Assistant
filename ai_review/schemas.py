from dataclasses import dataclass
from typing import List


@dataclass
class ReviewIssue:
    title: str
    description: str
    severity: str
    line: int
    suggestion: str


@dataclass
class AIReviewResult:
    file: str
    summary: str
    issues: List[ReviewIssue]
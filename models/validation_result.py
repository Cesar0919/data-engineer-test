from dataclasses import dataclass, field
from typing import List


@dataclass
class Violation:
    rule_id: str
    severity: str
    action: str
    message: str


@dataclass
class ValidationResult:
    status: str
    violations: List[Violation] = field(default_factory=list)
from models.validation_result import Violation
from rules.base_rule import BaseRule


class MinimumAmountRule(BaseRule):

    rule_id = "RG-001"
    severity = "CRITICAL"

    def validate(self, transaction: dict):

        amount = transaction.get("amount")

        if amount is None or amount <= 0:
            return Violation(
                rule_id=self.rule_id,
                severity=self.severity,
                action="FAIL",
                message="Amount must be greater than zero."
            )

        return None
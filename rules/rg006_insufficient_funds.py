from models.validation_result import Violation
from rules.base_rule import BaseRule


class InsufficientFundsRule(BaseRule):

    rule_id = "RG-006"
    severity = "CRITICAL"

    def validate(self, transaction: dict):

        tx_type = transaction.get("transaction_type")
        amount = transaction.get("amount")
        balance = transaction.get("balance_before")

        if tx_type in ["WITHDRAWAL", "TRANSFER"] and amount > balance:
            return Violation(
                rule_id=self.rule_id,
                severity=self.severity,
                action="FAIL",
                message="Insufficient funds."
            )

        return None
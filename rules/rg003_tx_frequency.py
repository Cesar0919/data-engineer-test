from models.validation_result import Violation
from rules.base_rule import BaseRule


class TransactionFrequencyRule(BaseRule):

    rule_id = "RG-003"
    severity = "CRITICAL"

    def validate(self, transaction: dict):

        tx_count = transaction.get("daily_tx_count")
        account_age = transaction.get("account_age_days")

        if tx_count > 20 and account_age < 30:
            return Violation(
                rule_id=self.rule_id,
                severity=self.severity,
                action="FAIL",
                message="High transaction frequency detected for new account."
            )

        return None
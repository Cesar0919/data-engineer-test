from config.settings import DAILY_LIMIT_USD
from models.validation_result import Violation
from rules.base_rule import BaseRule


class DailyLimitRule(BaseRule):

    rule_id = "RG-002"
    severity = "HIGH"

    def validate(self, transaction: dict):

        daily_total = transaction.get("daily_total_amount", 0)

        if daily_total > DAILY_LIMIT_USD:
            return Violation(
                rule_id=self.rule_id,
                severity=self.severity,
                action="FAIL",
                message=f"Daily transaction limit exceeded: {daily_total}"
            )

        return None
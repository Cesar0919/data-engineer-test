from config.settings import APPROVED_CURRENCIES
from models.validation_result import Violation
from rules.base_rule import BaseRule


class AllowedCurrencyRule(BaseRule):

    rule_id = "RG-004"
    severity = "MEDIUM"

    def validate(self, transaction: dict):

        currency = transaction.get("currency")

        if currency not in APPROVED_CURRENCIES:
            return Violation(
                rule_id=self.rule_id,
                severity=self.severity,
                action="FAIL",
                message=f"Currency {currency} is not allowed."
            )

        return None
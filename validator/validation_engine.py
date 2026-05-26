from models.validation_result import ValidationResult

from rules.rg001_min_amount import MinimumAmountRule
from rules.rg002_daily_limit import DailyLimitRule
from rules.rg003_tx_frequency import TransactionFrequencyRule
from rules.rg004_allowed_currency import AllowedCurrencyRule
from rules.rg005_high_risk_country import HighRiskCountryRule
from rules.rg006_insufficient_funds import InsufficientFundsRule
from rules.rg007_unusual_hours import UnusualHoursRule
from rules.rg008_schema_validation import SchemaValidationRule


class ValidationEngine:

    def __init__(self):

        self.rules = [
            SchemaValidationRule(),
            MinimumAmountRule(),
            DailyLimitRule(),
            TransactionFrequencyRule(),
            AllowedCurrencyRule(),
            HighRiskCountryRule(),
            InsufficientFundsRule(),
            UnusualHoursRule(),
        ]

    def validate(self, transaction: dict):

        violations = []

        for rule in self.rules:

            violation = rule.validate(transaction)

            if violation:

                violations.append(violation)

                # Short-circuit only for CRITICAL FAILS
                if (
                        violation.severity == "CRITICAL"
                        and violation.action == "FAIL"
                ):
                    return ValidationResult(
                        status="REJECTED",
                        violations=violations
                    )

        has_fail = any(v.action == "FAIL" for v in violations)
        has_review = any(v.action == "REVIEW" for v in violations)

        if has_fail:
            status = "REJECTED"

        elif has_review:
            status = "REVIEW"

        else:
            status = "APPROVED"

        return ValidationResult(
            status=status,
            violations=violations
        )
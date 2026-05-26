from config.settings import HIGH_RISK_COUNTRIES
from models.validation_result import Violation
from rules.base_rule import BaseRule


class HighRiskCountryRule(BaseRule):

    rule_id = "RG-005"
    severity = "CRITICAL"

    def validate(self, transaction: dict):

        country = transaction.get("country_code")

        if country in HIGH_RISK_COUNTRIES:
            return Violation(
                rule_id=self.rule_id,
                severity=self.severity,
                action="REVIEW",
                message=f"Transaction from high-risk country: {country}"
            )

        return None
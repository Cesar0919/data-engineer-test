from datetime import datetime

from config.settings import (
    UNUSUAL_HOUR_START,
    UNUSUAL_HOUR_END,
    UNUSUAL_AMOUNT_THRESHOLD
)

from models.validation_result import Violation
from rules.base_rule import BaseRule


class UnusualHoursRule(BaseRule):

    rule_id = "RG-007"
    severity = "LOW"

    def validate(self, transaction: dict):

        timestamp = transaction.get("timestamp")
        amount = transaction.get("amount")

        tx_datetime = datetime.fromisoformat(timestamp)
        hour = tx_datetime.hour

        if (
            UNUSUAL_HOUR_START <= hour <= UNUSUAL_HOUR_END
            and amount > UNUSUAL_AMOUNT_THRESHOLD
        ):
            return Violation(
                rule_id=self.rule_id,
                severity=self.severity,
                action="REVIEW",
                message="Transaction executed during unusual hours."
            )

        return None
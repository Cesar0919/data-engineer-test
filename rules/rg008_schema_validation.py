from config.settings import REQUIRED_FIELDS
from models.validation_result import Violation
from rules.base_rule import BaseRule


class SchemaValidationRule(BaseRule):

    rule_id = "RG-008"
    severity = "CRITICAL"

    def validate(self, transaction: dict):

        for field_name, expected_type in REQUIRED_FIELDS.items():

            if field_name not in transaction:
                return Violation(
                    rule_id=self.rule_id,
                    severity=self.severity,
                    action="FAIL",
                    message=f"Missing required field: {field_name}"
                )

            value = transaction[field_name]

            if value is None:
                return Violation(
                    rule_id=self.rule_id,
                    severity=self.severity,
                    action="FAIL",
                    message=f"Field {field_name} cannot be null"
                )

            if not isinstance(value, expected_type):
                return Violation(
                    rule_id=self.rule_id,
                    severity=self.severity,
                    action="FAIL",
                    message=f"Invalid type for field {field_name}"
                )

        return None
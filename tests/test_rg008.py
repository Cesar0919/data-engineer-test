from rules.rg008_schema_validation import SchemaValidationRule


def test_valid_schema():

    rule = SchemaValidationRule()

    transaction = {
        "transaction_id": "tx-001",
        "amount": 100.0,
        "account_id": "acc-001",
        "currency": "USD",
        "transaction_type": "TRANSFER",
        "timestamp": "2026-05-24T10:00:00",
        "country_code": "US",
        "account_age_days": 100,
        "daily_tx_count": 5,
        "balance_before": 1000.0
    }

    violation = rule.validate(transaction)

    assert violation is None


def test_invalid_schema():

    rule = SchemaValidationRule()

    transaction = {
        "transaction_id": None,
        "amount": 100
    }

    violation = rule.validate(transaction)

    assert violation is not None
    assert violation.rule_id == "RG-008"
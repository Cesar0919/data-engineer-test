from rules.rg003_tx_frequency import TransactionFrequencyRule


def test_valid_transaction_frequency():

    rule = TransactionFrequencyRule()

    transaction = {
        "daily_tx_count": 10,
        "account_age_days": 100
    }

    violation = rule.validate(transaction)

    assert violation is None


def test_invalid_transaction_frequency():

    rule = TransactionFrequencyRule()

    transaction = {
        "daily_tx_count": 25,
        "account_age_days": 10
    }

    violation = rule.validate(transaction)

    assert violation is not None
    assert violation.rule_id == "RG-003"
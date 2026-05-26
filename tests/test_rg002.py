from rules.rg002_daily_limit import DailyLimitRule


def test_valid_daily_limit():

    rule = DailyLimitRule()

    transaction = {
        "daily_total_amount": 30000
    }

    violation = rule.validate(transaction)

    assert violation is None


def test_invalid_daily_limit():

    rule = DailyLimitRule()

    transaction = {
        "daily_total_amount": 60000
    }

    violation = rule.validate(transaction)

    assert violation is not None
    assert violation.rule_id == "RG-002"
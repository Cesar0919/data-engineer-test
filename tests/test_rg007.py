from rules.rg007_unusual_hours import UnusualHoursRule


def test_normal_transaction_hour():

    rule = UnusualHoursRule()

    transaction = {
        "timestamp": "2026-05-24T10:00:00",
        "amount": 1000
    }

    violation = rule.validate(transaction)

    assert violation is None


def test_unusual_transaction_hour():

    rule = UnusualHoursRule()

    transaction = {
        "timestamp": "2026-05-24T03:00:00",
        "amount": 10000
    }

    violation = rule.validate(transaction)

    assert violation is not None
    assert violation.rule_id == "RG-007"
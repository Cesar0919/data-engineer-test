from rules.rg001_min_amount import MinimumAmountRule


def test_valid_amount():

    rule = MinimumAmountRule()

    transaction = {
        "amount": 100
    }

    violation = rule.validate(transaction)

    assert violation is None


def test_invalid_amount():

    rule = MinimumAmountRule()

    transaction = {
        "amount": -50
    }

    violation = rule.validate(transaction)

    assert violation is not None
    assert violation.rule_id == "RG-001"
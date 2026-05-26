from rules.rg004_allowed_currency import AllowedCurrencyRule


def test_valid_currency():

    rule = AllowedCurrencyRule()

    transaction = {
        "currency": "USD"
    }

    violation = rule.validate(transaction)

    assert violation is None


def test_invalid_currency():

    rule = AllowedCurrencyRule()

    transaction = {
        "currency": "BTC"
    }

    violation = rule.validate(transaction)

    assert violation is not None
    assert violation.rule_id == "RG-004"
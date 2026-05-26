from rules.rg006_insufficient_funds import InsufficientFundsRule


def test_valid_balance():

    rule = InsufficientFundsRule()

    transaction = {
        "transaction_type": "TRANSFER",
        "amount": 100,
        "balance_before": 500
    }

    violation = rule.validate(transaction)

    assert violation is None


def test_insufficient_funds():

    rule = InsufficientFundsRule()

    transaction = {
        "transaction_type": "WITHDRAWAL",
        "amount": 1000,
        "balance_before": 100
    }

    violation = rule.validate(transaction)

    assert violation is not None
    assert violation.rule_id == "RG-006"
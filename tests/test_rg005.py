from rules.rg005_high_risk_country import HighRiskCountryRule


def test_valid_country():

    rule = HighRiskCountryRule()

    transaction = {
        "country_code": "US"
    }

    violation = rule.validate(transaction)

    assert violation is None


def test_high_risk_country():

    rule = HighRiskCountryRule()

    transaction = {
        "country_code": "IR"
    }

    violation = rule.validate(transaction)

    assert violation is not None
    assert violation.rule_id == "RG-005"
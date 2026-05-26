import json

from validator.validation_engine import ValidationEngine


sample_transaction = {
    "transaction_id": "TX123",
    "amount": 7000.0,
    "account_id": "ACC100",
    "currency": "USD",
    "transaction_type": "TRANSFER",
    "timestamp": "2026-04-29T03:15:00",
    "country_code": "IR",
    "account_age_days": 10,
    "daily_tx_count": 25,
    "balance_before": 5000.0,
    "daily_total_amount": 60000
}


engine = ValidationEngine()

result = engine.validate(sample_transaction)

print(json.dumps({
    "status": result.status,
    "violations": [
        vars(v) for v in result.violations
    ]
}, indent=4))
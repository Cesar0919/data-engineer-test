APPROVED_CURRENCIES = ["USD", "DOP", "EUR", "CAD", "GBP"]

HIGH_RISK_COUNTRIES = ["IR", "KP", "SY", "AF"]

DAILY_LIMIT_USD = 50000

UNUSUAL_HOUR_START = 2
UNUSUAL_HOUR_END = 5

UNUSUAL_AMOUNT_THRESHOLD = 5000

REQUIRED_FIELDS = {
    "transaction_id": str,
    "amount": (float, int),
    "account_id": str,
    "currency": str,
    "transaction_type": str,
    "timestamp": str,
    "country_code": str,
    "account_age_days": int,
    "daily_tx_count": int,
    "balance_before": (float, int),
}
import json
import logging

import pandas as pd

from validator.validation_engine import ValidationEngine


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


INPUT_FILE = "data/transactions.csv"
OUTPUT_FILE = "data/validation_results.csv"


def preprocess_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply preprocessing transformations required by business rules.
    """

    # Convert timestamp safely
    df["timestamp"] = pd.to_datetime(
        df["timestamp"],
        errors="coerce"
    )

    # Extract transaction date
    df["transaction_date"] = df["timestamp"].dt.date

    # Compute daily total amount per account
    df["daily_total_amount"] = (
        df.groupby(
            ["account_id", "transaction_date"]
        )["amount"]
        .transform("sum")
    )

    return df


def serialize_violations(violations):
    """
    Convert violations list into JSON string.
    """

    return json.dumps([
        {
            "rule_id": v.rule_id,
            "severity": v.severity,
            "action": v.action,
            "message": v.message
        }
        for v in violations
    ])


def process_transactions():

    logging.info("Loading transactions dataset...")

    df = pd.read_csv(INPUT_FILE)

    logging.info(f"Loaded {len(df)} transactions.")

    df = preprocess_dataframe(df)

    engine = ValidationEngine()

    results = []

    approved_count = 0
    rejected_count = 0
    review_count = 0
    error_count = 0

    for index, row in df.iterrows():

        try:

            transaction = row.to_dict()

            # Convert timestamp back to ISO string
            if pd.notnull(transaction.get("timestamp")):
                transaction["timestamp"] = (
                    transaction["timestamp"].isoformat()
                )

            result = engine.validate(transaction)

            if result.status == "APPROVED":
                approved_count += 1

            elif result.status == "REJECTED":
                rejected_count += 1

            elif result.status == "REVIEW":
                review_count += 1

            enriched_row = transaction.copy()

            enriched_row["validation_status"] = result.status

            enriched_row["violations"] = serialize_violations(
                result.violations
            )

            results.append(enriched_row)

        except Exception as e:

            error_count += 1

            logging.error(
                f"Error processing row {index}: {str(e)}"
            )

    results_df = pd.DataFrame(results)

    results_df.to_csv(
        OUTPUT_FILE,
        index=False
    )

    logging.info("Batch validation completed.")
    logging.info(f"Total processed: {len(df)}")
    logging.info(f"Approved: {approved_count}")
    logging.info(f"Rejected: {rejected_count}")
    logging.info(f"Review: {review_count}")
    logging.info(f"Errors: {error_count}")

    logging.info(
        f"Validation results exported to: {OUTPUT_FILE}"
    )


if __name__ == "__main__":
    process_transactions()
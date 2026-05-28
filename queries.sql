-- =========================================
-- Q1: Top 10 cuentas con mayor monto total rechazado en los últimos 7 días
-- =========================================

SELECT
    account_id,
    SUM(amount) AS total_rejected_amount,
    COUNT(*) AS rejected_transactions
FROM validation_results
WHERE validation_status = 'REJECTED'
  AND timestamp >= CURRENT_TIMESTAMP - INTERVAL '7 days'
GROUP BY account_id
ORDER BY total_rejected_amount DESC
LIMIT 10;


-- =========================================
-- Q2: Tasa de rechazo por transaction_type y merchant_category (tabla pivote)
-- =========================================

SELECT
    transaction_type,
    merchant_category,

    COUNT(*) AS total_transactions,

    SUM(
        CASE
            WHEN validation_status = 'REJECTED'
            THEN 1
            ELSE 0
        END
    ) AS rejected_transactions,

    ROUND(
        100.0 *
        SUM(
            CASE
                WHEN validation_status = 'REJECTED'
                THEN 1
                ELSE 0
            END
        ) / COUNT(*),
        2
    ) AS rejection_rate_pct

FROM validation_results

GROUP BY
    transaction_type,
    merchant_category

ORDER BY rejection_rate_pct DESC;



-- =========================================
-- Q3: Regla más frecuente por país, usando window functions (RANK() o ROW_NUMBER())
-- =========================================

WITH exploded_rules AS (

    SELECT
        country_code,

        jsonb_array_elements(
            violations::jsonb
        ) ->> 'rule_id' AS rule_id

    FROM validation_results

),

rule_counts AS (

    SELECT
        country_code,
        rule_id,
        COUNT(*) AS violation_count

    FROM exploded_rules

    GROUP BY
        country_code,
        rule_id
),

ranked_rules AS (

    SELECT
        country_code,
        rule_id,
        violation_count,

        ROW_NUMBER() OVER (
            PARTITION BY country_code
            ORDER BY violation_count DESC
        ) AS rank_num

    FROM rule_counts
)

SELECT
    country_code,
    rule_id,
    violation_count

FROM ranked_rules

WHERE rank_num = 1

ORDER BY violation_count DESC;


-- =========================================
-- Q4: Cuentas con más de 3 transacciones REVIEW en las últimas 24 horas (query de alerta)
-- =========================================

SELECT
    account_id,
    COUNT(*) AS review_transactions

FROM validation_results

WHERE validation_status = 'REVIEW'
  AND timestamp >= CURRENT_TIMESTAMP - INTERVAL '24 hours'

GROUP BY account_id

HAVING COUNT(*) > 3

ORDER BY review_transactions DESC;
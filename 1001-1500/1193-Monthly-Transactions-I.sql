SELECT      CONCAT(YEAR(trans_date), "-", IF(MONTH(trans_date) < 10, "0", ""), MONTH(trans_date)) AS month, 
            country, 
            COUNT(*) as trans_count,
            SUM(IF(state = "approved", 1, 0)) AS approved_count,
            SUM(amount) AS trans_total_amount,
            SUM(IF(state = "approved", amount, 0)) AS approved_total_amount
FROM        Transactions
GROUP BY    month, country;
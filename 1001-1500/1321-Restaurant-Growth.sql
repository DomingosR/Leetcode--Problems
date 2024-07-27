SELECT      DaySumA.visited_on,
            SUM(DaySumB.DaySum) AS amount,
            ROUND(AVG(DaySumB.DaySum), 2) AS average_amount
FROM        (SELECT    visited_on,
                       SUM(amount) AS DaySum
             FROM      Customer
             GROUP BY  visited_on
            ) AS DaySumA
JOIN        (SELECT    visited_on,
                       SUM(amount) AS DaySum
             FROM      Customer
             GROUP BY  visited_on
            ) AS DaySumB
WHERE       DATEDIFF(DaySumA.visited_on, DaySumB.visited_on) BETWEEN 0 AND 6
GROUP BY    DaySumA.visited_on
HAVING      COUNT(DaySumB.visited_on) = 7;
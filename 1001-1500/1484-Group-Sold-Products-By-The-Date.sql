SELECT      sell_date,
            COUNT(DISTINCT(product), sell_date) AS num_sold, 
            GROUP_CONCAT(DISTINCT product ORDER BY product) AS products
FROM        Activities
GROUP BY    sell_date;
SELECT      Sales1.product_id, Sales1.year as first_year, Sales1.quantity, Sales1.price
FROM        Sales as Sales1
JOIN        (SELECT   product_id, MIN(year) AS minYear
             FROM     Sales AS Sales2
             GROUP BY product_id) AS minSaleYear
WHERE       Sales1.year = minSaleYear.minYear
AND         Sales1.product_id = minSaleYear.product_id;
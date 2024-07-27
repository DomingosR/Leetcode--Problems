SELECT    product_id, COALESCE(ROUND(SUM(units * price) / SUM(units), 2), 0) AS average_price
FROM      (SELECT     Prices.product_id, UnitsSold.units, Prices.price
           FROM       UnitsSold
           RIGHT JOIN Prices
           ON         UnitsSold.product_id = Prices.product_id
           AND        UnitsSold.purchase_date BETWEEN Prices.start_date AND Prices.end_date
          ) AS Sales
GROUP BY  product_id;

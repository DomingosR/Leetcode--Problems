(SELECT      product_id, 10 as price
 FROM        Products as Prod1
 GROUP BY    product_id
 HAVING      MIN(change_date) > "2019-08-16")
UNION
(SELECT      Prod2.product_id, Prod2.new_price as price
 FROM        Products as Prod2
 JOIN        (SELECT   product_id, MAX(change_date) AS ChangeDate
              FROM     Products as Prod3
              WHERE    change_date <= "2019-08-16"
              GROUP BY product_id
             ) AS MaxChangeDate
 ON          Prod2.product_id = MaxChangeDate.product_id
 AND         Prod2.change_date = MaxChangeDate.ChangeDate);
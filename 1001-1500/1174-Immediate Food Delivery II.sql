SELECT      ROUND(AVG(IF(order_date = customer_pref_delivery_date, 100, 0)), 2) AS immediate_percentage
FROM        Delivery
RIGHT JOIN  (SELECT      customer_id, MIN(order_date) AS first_order_date
             FROM        Delivery
             GROUP BY    customer_id
            ) as FirstDate
ON          Delivery.customer_id = FirstDate.customer_id
AND         Delivery.order_date = FirstDate.first_order_date;
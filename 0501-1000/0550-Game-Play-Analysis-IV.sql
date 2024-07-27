SELECT      ROUND(COUNT(DISTINCT A2.player_id) / COUNT(DISTINCT A1.player_id), 2) AS fraction
FROM        Activity AS A1
LEFT JOIN   Activity AS A2
ON          A2.player_id = A1.player_id
AND         DATEDIFF(A2.event_date, A1.event_date) = 1
WHERE       (A1.player_id, A1.event_date)
IN          (SELECT player_id, MIN(event_date)
             FROM Activity
             GROUP BY player_id
            );

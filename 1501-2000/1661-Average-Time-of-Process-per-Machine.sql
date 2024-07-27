SELECT A1.machine_id as machine_id, 
       ROUND(SUM(A2.timestamp - A1.timestamp)/COUNT(A2.timestamp - A1.timestamp), 3) as processing_time
FROM Activity as A1, Activity as A2
WHERE A1.machine_id = A2.machine_id
AND A1.process_id = A2.process_id
AND A1.activity_type = 'start'
AND A2.activity_type = 'end'
GROUP BY A1.machine_id;
SELECT W1.id as Id
FROM Weather as W1, Weather as W2
WHERE DATEDIFF(W1.recordDate, w2.recordDate) = 1
AND W1.temperature > W2.temperature;
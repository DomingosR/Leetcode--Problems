SELECT      DISTINCT Logs1.num AS ConsecutiveNums
FROM        Logs AS Logs1
JOIN        Logs AS Logs2
ON          Logs2.id = Logs1.id + 1
JOIN        Logs AS Logs3
ON          Logs3.id = Logs2.id + 1
WHERE       Logs1.num = Logs2.num
AND         Logs2.num = Logs3.num;
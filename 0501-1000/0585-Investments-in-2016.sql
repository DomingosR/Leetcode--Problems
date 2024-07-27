SELECT      ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM        Insurance AS InsA
WHERE       1 = (SELECT COUNT(*)
                 FROM   Insurance as InsB
                 WHERE  InsA.lat = InsB.lat
                 AND    InsA.lon = InsB.lon
                )
AND         1 < (SELECT COUNT(*)
                 FROM   Insurance as InsC
                 WHERE  InsA.tiv_2015 = InsC.tiv_2015
                );
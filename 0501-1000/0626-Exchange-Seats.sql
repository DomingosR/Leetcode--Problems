SELECT      RANK() OVER (ORDER BY IF(MOD(id, 2) = 0, id - 1, id + 1)) AS id,
            student
FROM        seat;
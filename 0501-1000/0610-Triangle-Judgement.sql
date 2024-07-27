SELECT      *, IF(x < y + z AND y < x + z AND z < x + y, "Yes", "No") as "Triangle"
FROM        Triangle;
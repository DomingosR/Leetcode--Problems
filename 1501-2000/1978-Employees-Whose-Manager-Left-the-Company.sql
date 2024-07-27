SELECT      Empl1.employee_id
FROM        Employees AS Empl1
LEFT JOIN   Employees AS Empl2
ON          Empl1.manager_id = Empl2.employee_id
WHERE       Empl1.salary < 30000
AND         Empl1.manager_id IS NOT NULL
AND         Empl2.employee_id IS NULL
ORDER BY    Empl1.employee_id;

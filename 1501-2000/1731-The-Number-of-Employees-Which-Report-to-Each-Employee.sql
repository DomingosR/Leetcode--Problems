SELECT      Empl1.employee_id, 
            Empl1.name, 
            COUNT(*) as reports_count, 
            ROUND(AVG(Empl2.age), 0) as average_age
FROM        Employees AS Empl1
JOIN        Employees AS Empl2
ON          Empl1.employee_id = Empl2.reports_to
GROUP BY    Empl1.employee_id
ORDER BY    Empl1.employee_id;
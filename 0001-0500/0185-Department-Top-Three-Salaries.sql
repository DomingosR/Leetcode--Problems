SELECT Department.name as Department, EmployeesWithRank.name as Employee, EmployeesWithRank.salary as Salary 
FROM   Department
INNER JOIN 
       (
            SELECT 
                name,  
                departmentId,
                salary, 
                DENSE_RANK() OVER (
                    PARTITION BY departmentId
                    ORDER BY salary DESC) salaryRank
            FROM 
                Employee
       ) AS EmployeesWithRank
ON     Department.id = EmployeesWithRank.departmentId
WHERE  EmployeesWithRank.salaryRank <= 3;
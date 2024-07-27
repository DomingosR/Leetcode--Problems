SELECT     Manager.name
FROM       Employee
INNER JOIN Employee as Manager
ON         Employee.managerId = Manager.id
GROUP BY   Employee.managerId
HAVING     COUNT(Employee.id) >= 5;
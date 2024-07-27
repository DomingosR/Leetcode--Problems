SELECT      contest_id, ROUND(100 * CountPerContest / UserCount, 2) as percentage
FROM        (SELECT     contest_id, COUNT(user_id) AS CountPerContest
             FROM       Register
             GROUP BY   contest_id
            ) as UsersPerContest
CROSS JOIN
            (SELECT COUNT(*) AS UserCount
             FROM Users) as TotalUsers
ORDER BY    percentage DESC, contest_id;
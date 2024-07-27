SELECT        id1 AS id, COUNT(id2) AS num
FROM          (
               (SELECT      accepter_id AS id1, requester_id as id2
                FROM        RequestAccepted)
                UNION
               (SELECT      requester_id AS id1, accepter_id as id2
                FROM        RequestAccepted)
              ) AS AllFriends
GROUP BY      id
ORDER BY      num DESC
LIMIT         1;
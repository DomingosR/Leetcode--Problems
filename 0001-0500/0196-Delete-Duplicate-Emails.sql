DELETE      PA
FROM        Person PA, Person PB
WHERE       PA.id > PB.id
AND         PA.email = PB.email;
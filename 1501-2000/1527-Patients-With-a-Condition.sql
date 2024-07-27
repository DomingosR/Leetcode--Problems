SELECT      *
FROM        Patients
WHERE       conditions LIKE '% DIAB1%'
OR          LEFT(conditions, 5) = 'DIAB1';
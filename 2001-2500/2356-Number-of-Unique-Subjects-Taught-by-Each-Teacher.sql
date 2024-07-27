SELECT      Teacher.teacher_id, COUNT(DISTINCT(subject_id)) AS cnt
FROM        Teacher
GROUP BY    Teacher.teacher_id;

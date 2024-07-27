SELECT Students2.*, COALESCE(Examinations2.attended_exams, 0) AS attended_exams
FROM (
      SELECT *
      FROM Students
      CROSS JOIN Subjects
     ) as Students2
LEFT JOIN (
      SELECT student_id, subject_name, COUNT(*) AS attended_exams
      FROM Examinations
      GROUP BY student_id, subject_name
     ) as Examinations2
ON Students2.student_id = Examinations2.student_id
AND Students2.subject_name = Examinations2.subject_name
GROUP BY Students2.student_id, Students2.subject_name
ORDER BY Students2.student_id, Students2.subject_name;

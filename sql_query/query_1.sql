-- Найти 5 студентов с наибольшим средним баллом по всем предметам.

SELECT ROUND(AVG(m.mark)), s.first_name, s.last_name FROM marks m
LEFT JOIN students AS s ON m.students_id = s.id
GROUP BY s.first_name, s.last_name
ORDER BY AVG(m.mark)
DESC LIMIT 5

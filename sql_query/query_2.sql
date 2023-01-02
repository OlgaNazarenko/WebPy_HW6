-- Найти студента с наивысшим средним баллом по определенному предмету.

SELECT discipline, round(AVG(m.mark)), s.first_name, s.last_name
FROM marks m
LEFT JOIN students AS s ON m.students_id = s.id
LEFT JOIN discipline AS d ON m.discipline_id = d.id
GROUP BY s.first_name, s.last_name, d.id, d.discipline
ORDER BY d.id
DESC LIMIT 1

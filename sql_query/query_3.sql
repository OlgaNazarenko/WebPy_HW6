-- Найти средний балл в группах по определенному предмету.

SELECT AVG(m.mark) FROM marks m
LEFT JOIN students AS s ON m.students_id = s.id
ORDER BY s.group_id

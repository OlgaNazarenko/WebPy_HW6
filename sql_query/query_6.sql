-- Найти список студентов в определенной группе.

SELECT s.last_name, s.first_name
FROM students AS s
WHERE s.group_id = 1

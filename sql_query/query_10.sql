-- Список курсов, которые определенному студенту читает
-- определенный преподаватель.

SELECT DISTINCT st.id, st.last_name, st.first_name, dis.discipline, pr.last_name
FROM students AS st
JOIN marks AS m ON m.students_id = st.id
JOIN discipline AS dis ON dis.id = m.discipline_id
JOIN professors AS pr ON pr.id = m.professors_id
WHERE st.id = 2 and pr.id = 2

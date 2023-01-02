-- Найти список курсов, которые посещает определенный студент.

SELECT distinct st.id, st.last_name, dis.discipline
FROM students AS st
JOIN marks AS m ON m.students_id = st.id
JOIN discipline AS dis ON dis.id = m.discipline_id
WHERE st.id = 3

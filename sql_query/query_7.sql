-- Найти оценки студентов в отдельной группе по определенному предмету.

SELECT st.last_name, st.group_id, m.mark, gr.title, dis.discipline
FROM students AS st
JOIN marks AS m ON m.students_id = st.id
JOIN discipline AS dis ON dis.id = m.discipline_id
JOIN groups AS gr ON st.group_id = gr.id
WHERE st.group_id = 2 and dis.id = 2
ORDER BY m.mark DESC

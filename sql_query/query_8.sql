-- Найти средний балл, который ставит определенный преподаватель
-- по своим предметам.

SELECT ROUND(AVG(m.mark)) as av_mark, pr.last_name
FROM professors AS pr
JOIN marks AS m ON professors_id = pr.id
WHERE pr.id = 5
ORDER BY av_mark, pr.last_name

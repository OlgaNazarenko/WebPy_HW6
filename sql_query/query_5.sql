-- Найти какие курсы читает определенный преподаватель.

SELECT distinct discipline AS d, last_name AS pr
FROM discipline
JOIN professors AS pr ON professors_id = pr.id

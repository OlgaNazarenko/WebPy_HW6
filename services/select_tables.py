import sqlite3
import os
from services.settings import SQL_QUERY, DATABASE


def select_tables(num) -> list:
    num = int(num)

    path_query = os.path.join(SQL_QUERY, f'query_{num}.sql')

    if not os.path.exists(path_query):
        return "Wrong entry"

    with open(path_query, 'r') as file:
        sql = file.read()

    with sqlite3.connect(DATABASE) as conn:
        cur = conn.cursor()
        cur.execute(sql)
        print(cur.fetchall())
        cur.close()

# sql = """
# SELECT DISTINCT st.id, st.last_name, st.first_name, dis.discipline, pr.last_name
# FROM students AS st
# JOIN marks AS m ON m.students_id = st.id
# JOIN discipline AS dis ON dis.id = m.discipline_id
# JOIN professors AS pr ON m.professors_id = pr.id
# WHERE st.id = 2 and pr.id = 2
# ;
# """


# if __name__ == '__main__':
#     print(select_tables(9))

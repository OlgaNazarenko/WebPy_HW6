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


# if __name__ == '__main__':
#     print(select_tables(9))

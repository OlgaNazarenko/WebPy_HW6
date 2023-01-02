import random
import sqlite3
import os
from faker import Faker
from random import randint
import datetime
from services.settings import DATABASE


sql_insert_student_table = "INSERT INTO students(first_name, last_name, group_id) VALUES(?, ?, ?)"
sql_create_group_table = "INSERT INTO groups(title) VALUES(?)"
sql_create_professor_table = "INSERT INTO professors(first_name, last_name) VALUES(?, ?)"
sgl_create_disciplines_table = "INSERT INTO discipline(discipline, groups_id, professors_id) VALUES(?, ?, ?)"
sql_create_marks_table = "INSERT INTO marks(mark, lesson_date, students_id, professors_id, discipline_id) " \
                         "VALUES(?, ?, ?, ?, ?)"


def fill_table() -> tuple():
    if os.path.exists(DATABASE):
        fake_data = Faker()

        with sqlite3.connect(DATABASE) as conn:
            cur = conn.cursor()

            # DB groups
            cur.execute('DELETE FROM groups')
            conn.commit()
            for _ in range(4):
                cur.execute(sql_create_group_table, (random.choice(['A', 'B', 'C', 'D'])))

            # DB student
            conn.commit()
            for _ in range(30):
                cur.execute(sql_insert_student_table, (fake_data.first_name(), fake_data.last_name(), random.randint(1, 4)))

            # DB professors
            for _ in range(5):
                cur.execute(sql_create_professor_table, (fake_data.first_name(), fake_data.last_name(),))

            # DB discipline
            for _ in range(8):
                cur.execute(sgl_create_disciplines_table,
                            (random.choice(['Python', 'Java', 'Korean', 'Japanese', 'QA']),
                             random.randint(1, 3), random.randint(1, 5),))

            # DB marks
            for _ in range(30):
                cur.execute(sql_create_marks_table,
                            (random.randint(1, 5), datetime.datetime.now().date() - datetime.timedelta(days=randint(0, 100)),
                             random.randint(1, 3), random.randint(1, 30),
                             random.randint(1, 5), ))

        cur.close()
        print("DB is completed \n")
    else:
        print('Incorrect')

#
# if __name__ == '__main__':
#     fill_table()
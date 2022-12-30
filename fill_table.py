import random
import sqlite3
import os
from faker import Faker
from create_tables import *
from random import choice , randint


sql_insert_student_table = "INSERT INTO students(first_name, last_name, group_id) VALUES(?, ?, ?)"
sql_create_group_table = "INSERT INTO groups(title) VALUES(?)"
sql_create_professor_table = "INSERT INTO professors(first_name, last_name) VALUES(?, ?)"
sgl_create_disciplines_table = "INSERT INTO discipline(discipline, groups_id, professors_id) VALUES(?, ?, ?)"
sql_create_marks_table = "INSERT INTO marks(mark, lesson_date, students_id, professors_is, discipline_id) " \
                         "VALUES(?, ?, ?, ?, ?, ?)"


def fill_tables():
    if os.path.exists('various.db'):
        fake_data = Faker()

        with sqlite3.connect('various.db') as conn:
            cur = conn.cursor()

            # DB groups
            cur.execute('DELETE FROM groups')
            conn.commit()
            for _ in range(4):
                cur.executemany(sql_create_group_table, (random.choice(['A', 'B', 'C', 'C'])))

            # DB student
            conn.commit()
            for _ in range(30):
                cur.executemany(sql_insert_student_table, (fake_data.first_name(), fake_data.last_name(), random.randint(1, 4)))

            # DB professors
            for _ in range(5):
                cur.executemany(sql_create_professor_table, (fake_data.first_name(), fake_data.last_name(),))

            # DB discipline
            for _ in range(8):
                cur.executemany(sgl_create_disciplines_table,
                            (random.choice(['Python', 'Java', 'Korean', 'Japanese', 'QA']),
                             random.randint(1, 3), random.randint(1, 5),))

            # DB marks
            for _ in range(30):
                cur.execute(sql_create_marks_table,
                            (random.randint(1,5), fake_data.date(), random.randint(1, 3), random.randint(1, 30),
                             random.randint(1, 5), ))

        cur.close()
        print("Completed \n")
    else:
        print('Incorrect')


if __name__ == '__main__':
    fill_tables()